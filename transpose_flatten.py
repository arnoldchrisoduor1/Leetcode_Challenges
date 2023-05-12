import numpy as np

# Read the dimensions of the matrix
x, y = map(int, input().split())

# Read the matrix from input
matrix = []
for i in range(x):
    row = list(map(int, input().split()))
    matrix.append(row)

# Convert the matrix to a NumPy array
my_array = np.array(matrix)

# Print the transpose of the matrix
print(np.transpose(my_array))

# Print the flattened version of the matrix
print(my_array.flatten())
