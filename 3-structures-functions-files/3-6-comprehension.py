# [expr for value in collection if condition] is equivalent to:
#
# result[]
# for value in collection:
#    if condition:
#        result.append(expr)

strings = ["a", "as", "bat", "car", "dove", "python"]
result = [x.upper() for x in strings if len(x) > 2]
print(f"Result: {result}")

# We can have comprehension also for dictionaries and sets
# dict_comp = {key-expr: value-expr for value in collection if condition}
# set_comp = {expr for value in collection if condition}
unique_lenghts = {len(x) for x in strings}
print(f"Unique lenghts: {unique_lenghts}")

loc_mapping = {value: index for index, value in enumerate(strings)}
print(f"As dictionary: {loc_mapping}")

# Nested list comprehensions
all_data = [["John", "Emily", "Michael", "Mary", "Steven"],
    ["Maria", "Juan", "Javier", "Natalia", "Pilar"]]
# If we want to have a single list containing all names with two or more a's...
names_of_interest = []
for names in all_data:
    enough_as = [name for name in names if name.count("a") >= 2]
    names_of_interest.extend(enough_as)

print(f"Names with 2 a's: {names_of_interest}")
# We can wrap this operation up in a single nested list comprehension
result = [name for names in all_data for name in names if name.count("a") >= 2]
print(f"Names with 2 a's: {result}")