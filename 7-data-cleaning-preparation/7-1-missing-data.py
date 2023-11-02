#For float64 dtype, pandas uses NaN, we call this sentinel value
import pandas as pd
import numpy as np

float_data = pd.Series([1.2, -3.5, np.nan, 0])

print(f'Float Data:\n{float_data}')

print(f'isNA:\n{float_data.isna()}')

#Python value None is also NA
string_data = pd.Series(["aardvark", np.nan, None, "avocado"])
print(f'String data:\n{string_data}')
print(f'isNA:\n{string_data.isna()}')


# dropna returns the series with only nonnull data and index values
data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(f'data:\n{data}')

print(f'dropna:\n{data.dropna()}')


# dropna removes all NaN data: both rows and columns if needed
data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],
                     [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])

print(f'data:\n{data}')
print(f'dropna:\n{data.dropna()}')

print(f'with how=all:\n{data.dropna(how="all")}')

# and to drop columns in the same way, pass axis="columns"
data[4] = np.nan
print(f'data:\n{data}')


print(f'with how=all:\n{data.dropna(axis="columns", how="all")}')

# we can use also thresh argument to keep rows containing at most a certain number of missing observations
df = pd.DataFrame(np.random.standard_normal((7, 3)))
df.iloc[:4, 1] = np.nan
df.iloc[:2, 2] = np.nan
print(f'data:\n{df}')
print(f'drop with thresh=2:\n{df.dropna(thresh=2)}')


################# filling missing data ######################
# fillna is the method to use
print(f'use fillna(0):\n{df.fillna(0)}')

# There are also interpolation methods that can be used
df = pd.DataFrame(np.random.standard_normal((6, 3)))
df.iloc[2:, 1] = np.nan
df.iloc[4:, 2] = np.nan
print(f'data:\n{df}')

print(f'method ffill:\n{df.fillna(method="ffill")}')
print(f'method ffill with limit of 2:\n{df.fillna(method="ffill", limit=2)}')