# ufunc or universal function performs element-wise operations on data in ndarrays
import numpy as np

arr = np.arange(10)
print(f"array = {array}")

print(f"array^2 = {np.sqrt(arr)}")
print(f"exp(array) = {np.exp(arr)}")

# functions like maximum or modf can return one array or two
rng = np.random.default_rng(seed=12345)

x = rng.standard_normal(8)
y = rng.standard_normal(8)
print(f"x = {x}")
print(f"y = {y}")

print(f"maximum = {np.maximum(x, y)}")

arr = rng.standard_normal(7) * 5
remainder, whole_part = np.modf(arr)

print(f"remainder = {remainder}")
print(f"whole_part = {whole_part}")

