array = [1, 6, 12, 7, 4, 9, 13]

less = []
greater = []
pivot = 6

for x in array:
    if x < pivot:
        less.append(x)
    else:
        greater.append(x)

print("less: ", less)

print("greater: ", greater)