# Example empty quantum circuit (bare bone)
from qiskit import *
from qiskit.visualization import plot_histogram

# Initialize circuit with 1 qubit and 1 classical bit
circ = QuantumCircuit(1, 1)

# Sets backend to the qasm_simulator
backend = Aer.get_backend('qasm_simulator')

# Maps Quantum bits to classical bits
circ.measure(range(1), range(1))

# Draws the emtpy circuit
circ.draw('mpl')

# Get the quantum program
job = execute(circ, backend, shots=1024)
result = job.result()
counts = result.get_counts(circ)
print("Total counts are: ", counts)

# Plots counts to histogram
plot_histogram(counts)

