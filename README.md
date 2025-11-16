# QHackathon25
A VQE simulation of CO₂ for Big Quantum Hackathon using real molecular integrals, demonstrating how variational quantum algorithms can support early studies in carbon-capture chemistry and showcase practical quantum methods for climate-focused research.

# 🌟 VQE for Quantum Chemistry

A minimal demonstration of using the **Variational Quantum Eigensolver (VQE)** to estimate molecular ground-state energies using **Hartree–Fock (HF)** initialization and the **UCCSD** ansatz.  
This project showcases how hybrid quantum-classical methods can simulate small molecules effectively.

---

## 📘 Overview
- Introduction to quantum chemistry  
- VQE formulation  
- HF initial-state construction  
- UCCSD ansatz  
- Example simulation (H₂)  

VQE uses parameterized quantum circuits and classical optimization to approximate the ground-state energy of a molecular Hamiltonian.

---

## 🔬 Quantum Chemistry Basics
The electronic structure problem is defined by the Schrödinger equation:

\[
\hat{H}|\Psi\rangle = E|\Psi\rangle
\]

Under the Born–Oppenheimer approximation, the Hamiltonian includes:
- electron kinetic energy  
- electron–nuclear attraction  
- electron–electron repulsion  
- nuclear repulsion  

---

## ⚡ VQE Method
VQE minimizes the expectation value:

\[
E(\theta) = \langle \Psi(\theta) | \hat{H} | \Psi(\theta) \rangle
\]

A parameterized circuit prepares the trial state, and measurements guide a classical optimizer to update parameters.

---

## 🧱 Hartree–Fock State
The HF reference wavefunction is:

\[
|\Psi_{HF}\rangle = \prod_{i=0}^{N-1} a_i^\dagger |0\rangle
\]

Mapped to qubits, this becomes applying **X-gates** to the initially occupied orbitals.

---

## 🔗 UCCSD Ansatz
The UCCSD trial state is defined as:

\[
|\Psi\rangle = e^{(T - T^\dagger)} |\Psi_{HF}\rangle
\]

where \(T\) includes single and double excitations, mapped to qubit operators through standard fermion-to-qubit transformations.

---

## 🧪 Example: H₂ Simulation
The notebook demonstrates:
- Building the molecular Hamiltonian  
- Preparing the HF state  
- Constructing UCCSD excitation operators  
- Running VQE optimization  
- Plotting energy convergence  

---


