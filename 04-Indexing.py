import pandas as pd
# loc — Label-Based Indexing
# Use labels/names. Inclusive on BOTH ends.
df = pd.DataFrame({
"Name": ["Amit","Ravi","Suresh","Kiran","Anjali"],
"Age": [22, 25, 28, 30, 24],
"Salary": [30000, 35000, 42000, 50000, 38000]
})
# Single row by label
print(df.loc[0]) # row at index label 0
# Range of rows (INCLUSIVE of 2)
print(df.loc[0:2]) # rows 0,1,2
# Specific row + specific column
print(df.loc[1, "Salary"]) # 35000
# Multiple rows, multiple columns
print(df.loc[0:2, ["Name","Salary"]])
# Update a value
df.loc[0, "Salary"] = 40000

# iloc — Integer Position-Based Indexing
# Use integer positions (like Python lists). Exclusive on the END.
# First row
print(df.iloc[0])
# Rows 0,1 — columns 0,2 (stop is EXCLUSIVE)
print(df.iloc[0:2, [0, 2]])
# Last row
print(df.iloc[-1])
# First 3 rows, all columns
print(df.iloc[:3, :])
# All rows, last 2 columns
print(df.iloc[:, -2:])