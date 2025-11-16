# QHackathon25
A VQE simulation of CO₂ for Big Quantum Hackathon using real molecular integrals, demonstrating how variational quantum algorithms can support early studies in carbon-capture chemistry and showcase practical quantum methods for climate-focused research.

🌟 VQE for Quantum Chemistry

A simple and structured demonstration of using the Variational Quantum Eigensolver (VQE) to estimate molecular ground-state energies using Hartree–Fock initialization and the UCCSD ansatz.
This project highlights how hybrid quantum–classical methods can simulate small molecules efficiently.

📘 Overview

Intro to quantum chemistry

VQE formulation

HF initial-state preparation

UCCSD ansatz

Example simulation (H₂)

VQE leverages the variational principle to approximate the ground-state energy using parameterized circuits optimized by a classical optimizer.

🔬 Quantum Chemistry

The molecular wavefunction satisfies:

𝐻
^
∣
Ψ
⟩
=
𝐸
∣
Ψ
⟩
H
^
∣Ψ⟩=E∣Ψ⟩

Under the Born–Oppenheimer approximation, the Hamiltonian includes electron kinetic energy, electron–nuclear attraction, electron–electron repulsion, and nuclear repulsion.

⚡ VQE Method

VQE minimizes:

𝐸
(
𝜃
)
=
⟨
Ψ
(
𝜃
)
∣
𝐻
^
∣
Ψ
(
𝜃
)
⟩
E(θ)=⟨Ψ(θ)∣
H
^
∣Ψ(θ)⟩

A parameterized circuit prepares the trial state, and measurement results guide classical optimization.

🧱 Hartree–Fock State

The HF initial state:

∣
Ψ
𝐻
𝐹
⟩
=
∏
𝑖
=
0
𝑁
−
1
𝑎
𝑖
†
∣
0
⟩
∣Ψ
HF
	​

⟩=
i=0
∏
N−1
	​

a
i
†
	​

∣0⟩

In qubit form, this corresponds to applying X gates to occupied orbitals.

🔗 UCCSD Ansatz

The UCCSD trial state:

∣
Ψ
⟩
=
𝑒
(
𝑇
−
𝑇
†
)
∣
Ψ
𝐻
𝐹
⟩
∣Ψ⟩=e
(T−T
†
)
∣Ψ
HF
	​

⟩

Includes single and double excitations, mapped to qubits through fermion-to-qubit transformations.

🧪 Example: H₂

The notebook walks through:

Building the molecular Hamiltonian

Preparing HF reference

Constructing UCCSD operators

Running VQE optimization

Plotting convergence
