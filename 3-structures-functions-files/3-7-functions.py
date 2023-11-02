def my_function(x, y):
    return x + y
print(f"Result: {my_function(3, 4)}")

# keyword arguments are optional and they must be provided with a default value
def my_function2(x, y, z = 1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)

# we can use the keyword or not
print(my_function2(5, 6, z=0.7))
print(my_function2(3.14, 7, 3.5))
print(my_function2(10, 20))

# returning multipe values
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()

# Functions are objects, suppose we were doing some data cleaning
states = ["   Alabama", "Georgia!", "Georgia", "georgia", "Flo0rIda", 
    "south    carolina##", "West virginia?"]
# we can use re standard library module for regular expresions
import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub("[!#?]", "", value)
        value = value.title()
        result.append(value)
    return result

print(f"cleaned data: {clean_strings(states)}")

# other approach could be a list of functions
def remove_punctuation(value):
    return re.sub("[!#?]", "", value)

clean_ops = [str.strip, remove_punctuation, str.title]
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result

print(f"Cleaned: {clean_strings(states, clean_ops)}")

# Lambda functions
def apply_to_list(some_list, f):
    return[f(x) for x in some_list]
ints = [4, 0, 1, 5, 6]
print(f"transformed list: {apply_to_list(ints, lambda x: x * 2)}")