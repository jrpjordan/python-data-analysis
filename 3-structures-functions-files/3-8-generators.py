some_dict = {"a": 1, "b": 2, "c": 3}

for key in some_dict:
    print(key)

# Writing for key => python interpreter creates an iterator.
# Most methods expecting a list or list like object will also accept any iterable object.

dict_iterator = iter(some_dict)
print(list(dict_iterator))

# A generator is a way, similar to writing a normal function, to construct a new iterable object
# Whereas normal functions execute and return a single result at a time,
# generators can return a sequence of multiple values by pausing and resuming execution each time generator is used.

# The key word to use a generator is yield instead of return
def squares(n=10):
    print(f"Generating squares from 1 to {n ** 2}")
    for i in range(1, n + 1):
        yield i ** 2;

# calling a generator doesn't produce an inmediately execution
gen = squares()

# When you request elements from the generator is when it starts executing code
for x in gen:
    print(x)


# Generator expressions, other way to make genaretor is with generator expression.
# Using a list comprehension within parentheses

gen = (x ** 2 for x in range(100))

# It's equivales to...
def _make_gen():
    for x in range(100):
        yield x ** 2

gen2 = _make_gen()

# Generators can be used as function arguments
print(sum(x ** 2 for x in range(100)))

print(dict((i, i ** 2) for i in range(5)))