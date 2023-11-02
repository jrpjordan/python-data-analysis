import itertools

def first_letter(x):
    return x[0]

names = ["Alan", "Adam", "Wes", "Will", "Steven", "Albert"]

print("Grouped elements by return value of first_letter() function")
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names is a generator