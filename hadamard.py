# Hadamard superposition demonstration
# A 50/50 balance should occur due to how the Hadamard's superpositions will collapse
from qiskit import *

# Defines backend as qasm_simulator
backend = Aer.get_backend('qasm_simulator')

# Creates circuit
q = QuantumRegister(1)
c = ClassicalRegister(1)
circ = QuantumCircuit(q, c)
circ.h(q)
circ.measure(q, c)

# Executes and outputs results
job = execute(circ, backend, shots=1024)
result = job.result()
print(result.get_counts(circ))

