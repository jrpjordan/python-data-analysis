import pandas as pd
import numpy as np
# DataFrame method drop_duplicates returns a DataFrame with rows where the duplicated array is false filtered out
data = pd.DataFrame({"k1": ["one", "two"] * 3 + ["two"],
                     "k2": [1, 1, 2, 3, 3, 4, 4]})

print(f'Data:\n{data}')

print(f'Drop duplicates:\n{data.drop_duplicates()}')

# we can use one column for example...
data["v1"] = range(7)
print(f'Data:\n{data}')
print(f'Drop duplicates one column:\n{data.drop_duplicates(subset=["k1"])}')

# we can also use the last repeated value
print(f'Drop k1 and k2 values but keeping last one:\n{data.drop_duplicates(["k1", "k2"], keep= "last")}')


################ DATA TRANFORMATION #############
print("################ DATA TRANFORMATION #############")
data = pd.DataFrame({"food": ["bacon", "pulled pork", "bacon",
                              "pastrami", "corned beef", "bacon",
                              "pastrami", "honey ham", "nova lox"],
                              "ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(f'Data:\n{data}')

# we want to add a column indicating the animal of procedence
meat_to_animal = {
    "bacon": "pig",
    "pulled pork": "pig",
    "pastrami": "cow",
    "corned beef": "cow",
    "honey ham": "pig",
    "nova lox": "salmon"
}

data["animal"] = data["food"].map(meat_to_animal)
print(f'Data:\n{data}')

# we could also use a function
def get_animal(x):
    return meat_to_animal[x]

print(f'data transformed:\n {data["food"].map(get_animal)}')


####### REPLACE #######
print("####### REPLACE #######")
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(f'Data:\n{data}')
print(f'Replaced:\n{data.replace([-999, -1000], np.nan)}')
