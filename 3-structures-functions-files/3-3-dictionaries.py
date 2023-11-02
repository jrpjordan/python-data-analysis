# dictionaries are hash maps, collection of key-value pairs
empty_dict = {}
d1 = {"a": "some value", "b": [1, 2, 3, 4]}
d1[7] = "an integer"
d1["dummy"] = "another value"
d1[5] = "some value"

print(d1)

# del to remove elements and pop to remove it and retrieve
del d1[5]

ret = d1.pop("dummy")
print(d1)
print(ret)

# keys and values gives you iterators
print(list(d1.keys()))
print(list(d1.values()))

# we can merge dictionaries, and discard old keys
d1.update({"b": "foo", "c": 12})
print(d1)

# a dictionary is a collection of 2-tuples, so the function dict accepts a list of 2-tuples
tuples = zip(range(5), reversed(range(5)))
mapping = dict(tuples)
print(mapping)