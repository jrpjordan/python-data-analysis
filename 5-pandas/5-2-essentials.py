import pandas as pd
import numpy as np
########### REINDEXING ###################

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
print(f"Obj = {obj}")

# Reindexing rearrages the data according to the new index
obj2 = obj.reindex(["a", "b", "c", "d", "e"])
print(f"Obj2 = {obj2}")

# We can interpolate missing data. Eg: ffill  forward-fills the values...
obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
obj3 = obj3.reindex(np.arange(6), method="ffill")
print(f"obj3 fullfilled = {obj3}")

# When we passed a sequence, it reindexes the rows in the result...
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=["a", "c", "d"],
                     columns=["Ohio", "Texas", "California"])

print(f"Frame = {frame}")
frame2 = frame.reindex(index=["a", "b", "c", "d"])
print(f"Frame2 = {frame2}")

## Dropping entries from an axis
obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
print(f"obj = {obj}")
obj2 = obj.drop(["d", "c"])
print(f"obj drop = {obj2}")

###################################################
print("##############################################")
# We can drop columns and axis
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index = ["Ohio", "Colorado", "Utah", "New York"],
                    columns = ["one", "two", "three", "four"])
print(f"data = {data}")

data2 = data.drop(index = ["Colorado", "Ohio"])
print(f"data droped by index = {data2}")

data3 = data.drop(columns = ["two"])
print(f"data dropped by column = {data3}")

######### Indexing, selection and filtering  ###############
print("###############")
obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
print(obj)

print(obj["b"])
print(obj[1])
print(obj[2:4])
print(obj[["b", "a", "d"]])
print(obj[[1, 3]])
print(obj[obj < 2])

# Better user loc and iloc. iloc ==> use integer index wether the index is an integer or not
obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])
obj2 = pd.Series ([1, 2, 3], index=["a", "b", "c"])

# obj2.loc([0, 1]) will fail as index are not numbers
print(obj1.iloc[[0, 1, 2]])
print(obj2.iloc[[0, 1, 2]])

print("#####################################")
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])

print(f"Data = {data}")

print(f'data(2) = {data["two"]}')
print(f'data[3,1] = {data[["three", "one"]]}')

print(f'data[:2] = {data[:2]}')
print(f'data[data[three] > 5] = {data[data["three"] > 5]}')

# boolean mask
data[data < 5] = 0
print(f'data < 5 = {data}')

print("###################### loc and iloc ####################")
print(data)
print(f'data from Colorado:\n{data.loc["Colorado"]}')
# Separating selections with comma is the way to combine rows and cols
print(f'data from Colorado, columns two and three:\n{data.loc["Colorado", ["two", "three"]]}')
print(f'using iloc to choose Utah and reorder the columns:\n{data.iloc[2, [3, 0, 1]]}')
# both iloc and loc works with slices in addition to single labels or lists of labels...
print(f'data from begining to Utah, column two:\n{data.loc[:"Utah", "two"]}')
print(f'data with all rows, from begining to third column where column three is greater than 5:\n{data.iloc[:, :3][data.three > 5]}')


################# ARITHMETIC AND DATA ALIGNMENT ##################################
print("##########################################################")
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), 
                   columns=["b", "c", "d"],
                   index=["Ohio", "Texas", "Colorado"])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), 
                   columns=["b", "d", "e"],
                   index=["Utah", "Ohio", "Texas", "Oregon"])
print(f'Data Frame 1:\n{df1}')
print(f'Data Frame 2:\n{df2}')
# sum dataframe is the unions of each
print(f'df1 + df2:\n{df1 + df2}')

# fill values
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list("abcd"))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list("abcde"))
df2.loc[1, "b"] = np.nan
print(f'Data Frame 1:\n{df1}')
print(f'Data Frame 2:\n{df2}')
# The sum of the frames will show the union...
print(f'Sum df1 and df2 :\n{df1 + df2}')
#but we can replace NaN places...
df3 = df1.add(df2, fill_value=0)
print(f'Sum of df1 and df2 replacing missing values:\n{df3}')