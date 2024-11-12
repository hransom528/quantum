# Harris Ransom
# Quantum Info Sci HW P2
# 11/13/2024

# Imports
import numpy as np

# Gets the degree of a check node
def getCheckNodeDegree(A, node):
	degree = np.sum(A[:, node])
	return degree

# Set up adjacency matrix and message
print("Setting up Tanner graph parameters...")
VARIABLE_NODES = 2000
CHECK_NODES = 1000
A = np.zeros((VARIABLE_NODES, CHECK_NODES)) # Adjacency matrix
m = np.zeros(VARIABLE_NODES) # Message (all zeros)

# Distribute connections between variable and check nodes
# Rows: 3 (degree 3)
# Cols: 6 (check 6)
print("Generating (3;6) Tanner graph...")
colCounts = np.zeros(CHECK_NODES) # Tracks how many columns are full
availableNodes = np.arange(0, CHECK_NODES)

# TODO: Fix adjacency matrix generation
for i in range(0, VARIABLE_NODES):
	chosenCols = [] # Used to check for duplicates
	for k in range(3):
		# Get random check node edge (column) to add
		randCol = np.random.choice(availableNodes)
		while ((colCounts[randCol] == 6) or (randCol in chosenCols)):
			randCol = np.random.choice(availableNodes)
			
		print(f"Finished picking column {k} for node {i}")
		# Add chosen column to duplicate tracker, column count tracker, and adjacency matrix
		chosenCols.append(randCol)
		colCounts[randCol] += 1 # TODO: Fix colCounts
		if (colCounts[randCol] == 6):
			np.delete(availableNodes, randCol)

		# Check for duplicate values
		if (A[i, randCol] == 1):
			raise ValueError(f"Duplicate for variable node {i}")
		
		# Create adjacency matrix edge
		A[i, randCol] = 1

	# Check for bad colCounts
	for i in range(0, len(colCounts)):
		if (colCounts[i] > 6):
			raise ValueError("Impossible colCount!")
		
# Verify that distribution criteria is met for Tanner Graph
print("Checking graph criteria...")
for i in range(0, VARIABLE_NODES):
	rowSum = sum(A[i, :])
	if (rowSum != 3):
		raise ValueError(f"Incorrect degree count for variable node {i} ({rowSum})")
for i in range(0, CHECK_NODES):
	nodeDegree = getCheckNodeDegree(A, i)
	if (nodeDegree != 6):
		raise ValueError(f"Incorrect degree count for check node {i} ({nodeDegree})")
print("All criteria passed")

# Create base copy of A to restore after each sim run
A_start = A

# Simulates different erasure rates
# Erasures simulated by -1 value
for epsilon in np.arange(0.005, 1, 0.005):
	print(f"Simulating erasure rate epsilon={epsilon}")

	# Reset adjacency matrix
	A = A_start

	# Erase nodes at rate epsilon
	m = np.random.choice([-1, 0], size=(VARIABLE_NODES), p=[epsilon, 1-epsilon])

	# Iterate until there are no more nodes to clean up
	continueFlag = True
	while (continueFlag):
		continueFlag = False
		
		# Erase received variable nodes
		k = 0
		while (k < len(m)):
			if (m[k] == 0):
				A = np.delete(A, k, axis=0) # Remove variable node row from adjacency matrix
				m = np.delete(m, k, axis=0) # Remove received node from vector
			else:
				k += 1
				
		# Check if m is empty
		if (m.size == 0):
			continueFlag = False
			break
		
		# Clean up degree-one check nodes
		for j in range(0, CHECK_NODES):
			if (getCheckNodeDegree(A, j) == 1):
				# Get index of unique neighbor
				ind = np.argwhere(A[:, j] == 1)
				
				# Substitute 0 into unique neighbor variable node
				m[ind] = 0
				
				# Set flag accordingly
				continueFlag = True

	# Determine whether or not erasure recovery fails based on continue flag
	# If m is empty, all nodes were recovered
	# If m is not empty, recovery was not successful
	if (m.size > 0):
		print(f"Max erasure rate simulated: {epsilon}")
		break