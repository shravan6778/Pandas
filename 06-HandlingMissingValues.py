import pandas as pd

#Detecting Missing Values
df = pd.DataFrame({
"Name": ["Amit", None, "Suresh"],
"Age": [22, None, 28],
"Salary": [30000, None, 42000],
"Score": [78, None, 85]
})
print(df.isnull()) # True/False mask for every cell
print(df.isnull().sum()) # count of NaN per column ‹ use this!
print(df.isnull().sum().sum()) # total NaN across the whole DataFrame
print(df.notnull()) # opposite of isnull()
# Percentage missing
print((df.isnull().sum() / len(df)) * 100)

#Dropping Missing Values — dropna()
# Drop ROWS that have any NaN
df.dropna(axis=0, inplace=True) # axis=0 = rows
# Drop COLUMNS that have any NaN
df.dropna(axis=1, inplace=True) # axis=1 = columns
# Drop rows only if ALL values are NaN
df.dropna(how="all", inplace=True)
# Drop rows where specific columns have NaN
df.dropna(subset=["Salary", "Age"], inplace=True)
# Keep rows that have at least N non-NaN values
df.dropna(thresh=3, inplace=True) # need at least 3 non-NaN

# Filling Missing Values — fillna()
# Fill with a constant
df.fillna(0, inplace=True)
# Fill numeric column with MEAN (most common for ML)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
# Fill with MEDIAN (better when data has outliers)
df["Age"].fillna(df["Age"].median(), inplace=True)
# Fill categorical column with MODE (most frequent value)
df["Department"].fillna(df["Department"].mode()[0], inplace=True)
# Forward Fill (ffill) — carry last valid value forward
# Great for time-series data
df["Price"].fillna(method="ffill", inplace=True)
# or: df["Price"].ffill(inplace=True) ‹ newer Pandas
# Backward Fill (bfill) — carry next valid value backward
df["Price"].fillna(method="bfill", inplace=True)

# Interpolation — interpolate()
# Best for: time-series / sequential numeric data with trends
data = {"Time": [1,2,3,4,5], "Value": [15, None, 30, None, 50]}
df = pd.DataFrame(data)
# Linear interpolation: estimates missing values on a straight line between
# surrounding known points fi NaN at index 1 becomes 22.5, at index 3 becomes 40
df["Value"] = df["Value"].interpolate(method="linear")
print(df)

