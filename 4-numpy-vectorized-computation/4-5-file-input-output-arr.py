import numpy as np

arr = np.arange(10)
np.save("some_array", arr)

arr2 = np.load("some_array.npy")
print(arr2)