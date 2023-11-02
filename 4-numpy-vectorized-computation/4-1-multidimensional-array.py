import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
print(data)

print(f"shape: {data.shape}")
print(f"type: {data.dtype}")
print(f"dim: {data.ndim}")

# Convert nested seqs into arrays
data2 =[[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)

# ways of initializing arrays
print(f"initi with zeros: {np.zeros(10)}")
print(f"empty: {np.empty((2, 3, 2))}")
print(f"range: {np.arange(15)}")

arr1 = np.array([1, 2, 3], dtype=np.int32)
float_arr = arr1.astype(np.float64)

# Slicing...
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(f"Slicing by first 2 rows: {arr2d[:2]}")
print(f"Slicing by rows and cols: {arr2d[:2, 1:]}")

# Boolean indexing
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

print(names == "Bob")
print(data[names == "Bob"])

# Fancy indexing
arr = np.zeros((8, 4))
for i in range(8):
    arr[i] = i

print(arr)

print("********** FANCY INDEXING *****************")
# Selecting a set of rows
print(arr[[4, 3, 0, 6]])
# Using negative indexes selects rows from the end
print(arr[[-3 -5, -7]])

# Passing multiple index arrays does something slightly different.
# Selects a one-dimensional array of elements corresponding to each tuple of indices

arr = np.arange(32).reshape((8, 4))
print(arr)
print(f"Multipe index arrays: {arr[[1, 5, 7, 2],[0, 3, 1, 2]]}")

# Transposing, T is the transposing of the matrix, and np. dot is the multiplication of matrix

arr = np.arange(15).reshape((3, 5))
print(f"arr = {arr}")

print(f"T(arr) = {arr.T}")

print(arr.T @ arr)