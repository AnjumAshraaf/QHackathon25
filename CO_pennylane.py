import pennylane as qml
from pennylane.qchem import fermionic_observable
import json
import numpy as np
from pennylane import jordan_wigner
# from pennylane import UCCSD  <--- DELETE THIS LINE
from pennylane.qchem import excitations
from pennylane.qchem import hf_state
from pennylane.qchem import excitations_to_wires
from pennylane import numpy as qnp
from pennylane.qchem import Molecule
from pennylane.qchem import molecular_hamiltonian
from pennylane.qchem import active_space
import optax
from jax import grad
import jax.numpy as jnp
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def read_xyz(filename):
    """Read symbols and coordinates (in Å) from an XYZ file."""
    with open(filename, "r") as f:
        lines = f.readlines()

    n = int(lines[0])
    symbols = []
    coords = []

    for line in lines[2:2+n]:
        s, x, y, z = line.split()
        symbols.append(s)
        coords.append([float(x), float(y), float(z)])

    return symbols, np.array(coords)


symbols, coordsA = read_xyz("CO.xyz")

electrons = 18
orbitals = 12

active_electrons = 4
active_orbitals = 4

molecule = Molecule(symbols, coordsA)
H, qubits = molecular_hamiltonian(
    molecule,
    active_electrons=active_electrons,
    active_orbitals=active_orbitals,
)
print("Number of qubits: {:}".format(qubits))
print("Qubit Hamiltonian")
print(H)

core, active = active_space(electrons, orbitals, active_electrons=active_electrons, active_orbitals=active_orbitals)

molecule = Molecule(
    symbols,
    coordsA,
    charge=0,
    mult=1,
    basis_name="sto-3g"
)

print("List of core orbitals: {:}".format(core))
print("List of active orbitals: {:}".format(active))
print("Number of qubits: {:}".format(2 * len(active)))

dev = qml.device("lightning.qubit", wires=qubits)

hf = qml.qchem.hf_state(active_electrons, qubits)


@qml.qnode(dev, interface="jax")
def circuit(param, wires):
    qml.BasisState(hf, wires=wires)
    qml.DoubleExcitation(param, wires=[0, 1, 4, 5])
    return qml.expval(H)


def cost_fn(param):
    return circuit(param, wires=range(qubits))


max_iterations = 100
conv_tol = 1e-10

opt = optax.sgd(learning_rate=0.01)

# theta = np.array(0.)
theta = jnp.array(0.0)

# store the values of the cost function
energy = [cost_fn(theta)]

# store the values of the circuit parameter
angle = [theta]

opt_state = opt.init(theta)

for n in range(max_iterations):

    gradient = grad(cost_fn)(theta)
    updates, opt_state = opt.update(gradient, opt_state)
    theta = optax.apply_updates(theta, updates)

    angle.append(theta)
    energy.append(cost_fn(theta))

    conv = np.abs(energy[-1] - energy[-2])

    print(f"Step = {n},  Energy = {energy[-1]:.8f} Ha")

    if conv <= conv_tol:
        break

print("\n" f"Final value of the ground-state energy = {energy[-1]:.8f} Ha")
print("\n" f"Optimal value of the circuit parameter = {angle[-1]:.4f}")

fig = plt.figure()
fig.set_figheight(5)
fig.set_figwidth(12)


# Add energy plot on column 1
ax1 = fig.add_subplot(121)
ax1.plot(range(n + 2), energy, color="purple", marker="o", ls="solid")
ax1.set_xlabel("Optimization step", fontsize=13)
ax1.set_ylabel("Energy (Hartree)", fontsize=13)
ax1.grid(True, linestyle="--", alpha=0.4)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax1.ticklabel_format(useOffset=False, style='plain', axis='y')

# Add angle plot on column 2
ax2 = fig.add_subplot(122)
ax2.plot(range(n + 2), angle, color="purple", marker="o", ls="solid")
ax2.set_xlabel("Optimization step", fontsize=13)
ax2.set_ylabel("Gate parameter $\\theta$ (rad)", fontsize=13)
ax2.grid(True, linestyle="--", alpha=0.4)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig("CO.png", dpi=300, bbox_inches="tight")
plt.show()
