import pandas as pd
from pandas import Series, DataFrame
import numpy as np




obj = Series([4, 7, -5, 3])
print(obj)

# We can get the array and index representation
print(obj.array)
print(obj.index)

# We can customize the index
obj2 = Series([4, 7, -5, 3], index = ["a", "b", "c", "d"])
print(obj2)
print(f"obj2[b] = {obj2['b']}")

# We can create a serie from a python dictonary
sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
obj3 = Series(sdata)
print(obj3)

# In the same way, we can convert a serie to a dictionary
print(obj3.to_dict())

# We can override the position of the index passing an index
states = ["California", "Ohio", "Oregon", "Texas"]
obj4 = pd.Series(sdata, index=states)

print(f"object4 = {obj4}")

# A usefull feature is to align series by index label in arithmetic operations
print(f"obj3 + obj4 = {obj3 + obj4}")

# Series and its index have a name attribute which integrates with other areas of pandas functionality
obj4.name = "population"
obj4.index.name = "state"
print(obj4)


####### DATA FRAME #####################################
print("########################### DATA FRAMES #####################################")

# Represents a rectangular table of data and contains an ordered, named collection of culumns, each of which can be a different value type.
# It can be thought of as a dictionary of Series all sharing the same index.

# 1. first way of build a data frame is from a dictionary of equal-length lists or NumPy arrays
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(f"frame: {frame}")

# we can define the order of the columns
print(pd.DataFrame(data, columns=["year", "state", "pop"]))

# we can retrieve one column from the data frame
print(frame["state"])

# to retrieve a specific row.
print(frame.loc[1])

#We can add new columns to the data frame and remove them with del keyword
frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])
frame2["eastern"] = frame2["state"] == "Ohio"
print(frame2)

del frame2["eastern"]
print(frame2.columns)

## Another common form of data is a nested dictionary of dictionaries
populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
               "Nevada": {2001: 2.4, 2002: 2.9}}

frame3 = pd.DataFrame(populations)
print(f"frame3 = {frame3}")

# Also we can traspose in the same way as numpy
print(f"frame3.T = {frame3.T}")