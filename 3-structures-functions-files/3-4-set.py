# unordered collection of unique elements.
a = set([2, 2, 2, 1, 3, 3])
print(f"a: {a}")

b = {1, 1, 5, 8, 8, 1}
print(f"b: {b}")

# They also support operations like union, intersection, difference...
print(f"a union b: {a.union(b)}")
print(f"a intersection b: {a.intersection(b)}")

# Elements in the set should be immutable and hashable, so it is good to convert them to a tuple
# We can also check subsets
a_set = {1, 2, 3, 4, 5}
print({1, 2, 3}.issubset(a_set))
