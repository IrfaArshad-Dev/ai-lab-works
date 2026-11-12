import numpy as np

# Creating a matrix
data = [[2, 5, 7], [-3, 4, 9]]
matrix_a = np.matrix(data)
print(matrix_a)

matrix_b = np.matrix('2, 4, 6 ; 5, 8, 10')
print(matrix_b)


# Multiplying two matrices
matrix_c = np.matrix([[2, 4, 6], [5, 7, 8]])
matrix_d = np.matrix([[3, 2], [4, 1], [6, 5]])

result = matrix_c.dot(matrix_d)
print(result)


# Transpose
array_a = np.array([[2, 3], [4, 5], [6, 7]])
print(array_a.transpose())


# Accessing array elements
numbers = np.array([3, 6, 9, 12, 15])

print("numbers[0] = ", numbers[0])
print("numbers[2] = ", numbers[2])
print("numbers[-1] = ", numbers[-1])


# Accessing elements in a 2D array
table = np.array([[3, 5, 7, 9, 11],
                  [4, 6, 8, 10, 12]])

print("table[0][4] = ", table[0][4])
print("table[1][1] = ", table[1][1])
print("table[-1][-2] = ", table[-1][-2])


# Accessing complete rows
grid = np.array([[2, 4, 6, 8],
                 [-3, 5, 7, 9],
                 [1, 3, 5, 7]])

print("grid[0] = ", grid[0])
print("grid[2] = ", grid[2])
print("grid[-1] = ", grid[-1])


# Accessing columns
print("First column = ", grid[:, 0])
print("Third column = ", grid[:, 2])
print("Last column = ", grid[:, -1])


# Copy an array
original = np.array([2, 4, 6, 8, 10])
copied = original.copy()

original[0] = 50

print("Original array after change:")
print(original)

print("Copied array:")
print(copied)


# View function changes both arrays
original = np.array([3, 6, 9, 12, 15])
viewed = original.view()

original[0] = 60

print("Original array after change:")
print(original)

print("Viewed array:")
print(viewed)


# Concatenate two arrays using axis = 1
first_array = np.array([[2, 4], [6, 8]])
second_array = np.array([[3, 5], [7, 9]])

combined = np.concatenate((first_array, second_array), axis=1)

print("Concatenated arrays (axis=1):")
print(combined)


# Concatenate two arrays
first_array = np.array([[2, 4, 6, 8]])
second_array = np.array([[3, 5, 7, 9]])

combined = np.concatenate((first_array, second_array))

print("Concatenated arrays:")
print(combined)


# Generating evenly spaced values
print("Evenly spaced values:")
print(np.linspace(2, 12))


# Creating a random array
random_array = np.random.random((1, 1))

print("Original Array:")
print(random_array)

minimum = random_array.min()
maximum = random_array.max()

print("Minimum Value:")
print(minimum)

print("Maximum Value:")
print(maximum)