import pandas as pd

# Reading csv with header
df = pd.read_csv("examples/ex1.csv")
print(f'Example 1 CSV with header:\n{df}')

# Reading csv with no header
df2 =pd.read_csv("examples/ex2.csv", header=None)
print(f'Example 2 CSV with no header:\n{df2}')

# We can as well using a column to be index
names = ["a", "b", "c", "d", "message"]
df3 = pd.read_csv("examples/ex2.csv", names=names, index_col="message")
print(f'Example 2 CSV with no headerand customizing indexes:\n{df3}')

# If we want a hierarchal index from multiple columns, pass a list of column numbers or names...

parsed = pd.read_csv("examples/csv_mindex.csv",
                     index_col=["key1", "key2"])
print(f'hierarchal index:\n{parsed}')

# In the cases of there is no delimiter, we can use a regular expression
result = pd.read_csv("examples/ex3.txt", sep="\s+")
print(f'space delimiter:\n{result}')

# we can skip rows
result = pd.read_csv("examples/ex4.csv", skiprows=[0, 2, 3])
print(f'File with comments:\n{result}')

# Reading large files in parts
result = pd.read_csv("examples/ex6.csv", sep="\s+", nrows=3)
print(f'large files, reading 3 rows only:\n{result}')

# Reading by chunks
chunker = pd.read_csv("examples/ex6.csv", sep="\s+", chunksize=3)
print('Writing chunks')
data = []
for piece in chunker:
    data.append(piece)
df = pd.concat(data, ignore_index=True)
print(df)

############################### EXPORTING DATA #####################################
result = pd.read_csv("examples/ex3.txt", sep="\s+")
result.to_csv("examples/out.csv")


############################### JSON DATA ###############################
obj = """
{"name": "Wes",
"cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
"pet": null,
"siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
             {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
}
"""

import json
result = json.loads(obj)
print(f'json object:\n{result}')
# dumps convert python object to json
asjson = json.dumps(result)

# Converting JSON object or list of objects to a DataFrame
siblings = pd.DataFrame(result["siblings"], columns=["name", "age"])
print(f'data frame from json:\n{siblings}')

############################### XML AND HTML: WEB SCRAPING #######################
tables = pd.read_html("examples/failed_bank_list.html")
failures = tables[0]
print(f'failures hed:\n{failures.head()}')

# counting the number of bank failures by year:
close_timestamps = pd.to_datetime(failures["Closing DateClosing"])
print(f'failures per year:\n{close_timestamps.dt.year.value_counts()}')