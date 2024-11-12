# CNOT Gate Demo
# Harris Ransom

# Imports
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Creates quantum circuit
circ = QuantumCircuit(2, 2)	# 2 classical, 2 qubits
circ.x(0)
circ.cx(0, 1)
circ.measure([0,1], [0,1])
circ.draw("mpl", filename="cnot.jpg")

# Run experiment
backend = Aer.get_backend("qasm_simulator")
result = execute(circ, backend, shots=1024).result()
counts = result.get_counts(circ)
print("Result: ", counts)
