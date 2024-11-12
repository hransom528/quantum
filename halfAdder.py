# Quantum Half Adder
# Harris Ransom

# Imports
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Build quantum circuit
circ = QuantumCircuit(4, 2)
circ.x(0)	# First qubit "1"
circ.x(1)	# Second qubit "1"
circ.cx(0, 2)
circ.cx(1, 2)
circ.ccx(0, 1, 3)
circ.measure(2, 0)
circ.measure(3, 1)
circ.draw("mpl", filename="halfAdder.jpg")

# Run simulation of circuit
backend = Aer.get_backend("qasm_simulator")
result = execute(circ, backend, shots=1024).result()
counts = result.get_counts(circ)
print("Input: 11")
print("Result: ", counts)
