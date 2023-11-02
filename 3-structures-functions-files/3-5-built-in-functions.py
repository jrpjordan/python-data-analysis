# enumerate: gives you the iterated variable and the value of the index-position in a loop
a = ["hello", "bannana", "car", "foo"]
for index, value in enumerate(a):
    print(f"index: {index}; value: {value}")

# sorted: sort the elements of a list
my_list = list("horse race")
print(sorted(my_list))

# zip: "pairs" up the elements of a number of lists, tuples or other sequences to create a list of tuples
seq1 = ["foo", "bar", "barz"]
seq2 = ["one", "two", "three"]
zipped = zip(seq1, seq2)
print(list(zipped))

# reversed: iterates over the elements of a sequence in reverse order
# reversed is a generator, so it doesn't create the reversed sequence until materialized
print(list(reversed(range(10))))