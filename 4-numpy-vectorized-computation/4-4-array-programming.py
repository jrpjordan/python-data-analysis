import numpy as np
import matplotlib.pyplot as plt

# np.meshgrid for evaluate a function eg. sqrt(x^2 + y^2) accross a regular grid of value
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

plt.show()

# conditional logic as array operations
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# result = [(x if c else y) for x,y,c in zip(xarr, yarr, cond)]

result = np.where(cond, xarr, yarr)
print(f"result: {result}")

#typical use
rng = np.random.default_rng(seed=12345)
arr = rng.standard_normal((4, 4))
print(np.where(arr > 0, 2, -2))

# Mathematical and statistical methods
# We can use them as a methods of the array object or from numpy module

arr = rng.standard_normal((5, 4))

print(f"arr = {arr}")
print(f"mean = {np.mean(arr)}")
print(f"sum = {arr.sum}")

print(f"mean columns = {arr.mean(axis=1)}")
print(f"mean rows = {arr.mean(axis=0)}")

# cumsum doesn't produce aggregates, it produces other vector
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(f"cumsum = {arr.cumsum()}")


# Methods for boolean arrays
arr = rng.standard_normal(100)

print((arr > 0).sum())  #number of positive values

bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())


# Unique and other set logic
names = np.array(["Bob", "Will", "Joe", "Bob", "Will", "Joe", "Joe"])
print(np.unique(names))


values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6])) #Returns true if the value in values is on the 2, 3, 6 array
