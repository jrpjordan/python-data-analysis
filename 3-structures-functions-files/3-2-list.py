# List are mutable, on the contrary than tuples

a_list = [2, 3, 7, None]
tup = ("foo", "bar", 2)
b_list = list(tup)
print(b_list)

# Some built-in functions
gen = range(10)
print(list(gen))

gen_odd = range(0, 10, 2)
print(list(gen_odd))

gen_reverse = range(10, 0, -1)
print(list(gen_reverse))

b = ['foo', 'peekabo', 'baz']
b.append('dwarf')
b.insert(1, "red")
print(b)

# wec can do the reverse of insert
print(b.pop(2))
print(b)

b.append('foo')
b.remove('foo')
print(b)

if "dwarf" in b:
    print("dwarf is in list")
else:
    print("dwarf is not in the list")

# we can concatenate lists
x = [4, None, "foo"]
print(x + [7, 8, (2, 3)])

x.extend([7, 8, (2, 3)])
print(x)

# there are ways to sort the list
a = [7, 2, 5, 1, 3]
a.sort()
print(a)

c = ["saw", "small", "He", "foxes", "six"]
c.sort(key=len)
print(c)

# Slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5])
print(seq[:5])
print(seq[3:])

# steps
print(seq[::2])
print(seq[::-1])