# fixed-length, immutable sequence of Python objects which, once assigned, cannot be changed

tup = (4, 5, 6)

# we cam convert any sequence or iterator to a tuple

tup_strings = tuple('string')
print(tup_strings)

# nested tup
nested_tup = (4, 5, 6), (7, 8)

print(nested_tup)
print(nested_tup[0])
print(nested_tup[1])

#unpackaging tuple
a, b, c = tup
print(b)

a, (b, c) = nested_tup;
print(b)

# common use is iteration over sequences of tuples or lists
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(f"a={a}, b={b}, c={c}")

# Other use is to pluck a few elements from the begining of a tuple
# It's a convention to use _ for non wanted values
values = 1, 2, 3, 4, 5, 6

a, b, *_ = values

print(f"a={a}")
print(f"b={b}")
print(f"rest={_}")