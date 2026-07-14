import pandas as pd
df = pd.DataFrame({
"Dept": ["IT","HR","Finance","IT","HR","IT","Finance","IT"],
"City": ["Hyd","Hyd","Mumbai","Hyd","Blr","Mumbai","Hyd","Blr"],
"Salary": [30000,35000,42000,50000,38000,45000,52000,60000]
})
# value_counts() — frequency of each unique value 
print(df["Dept"].value_counts())

# Normalise (proportions)
print(df["Dept"].value_counts(normalize=True))

# Sort ascending (least common first)
print(df["Dept"].value_counts(ascending=True))
# Include NaN in count
print(df["Dept"].value_counts(dropna=False))
# value_counts on multiple columns (cross-frequency)
print(df.groupby(["Dept","City"]).size())

# unique() — returns array of unique values 
print(df["Dept"].unique()) # array(['IT', 'HR', 'Finance'])
print(df["City"].unique()) # order of first appearance
# nunique() — count of unique values 
print(df["Dept"].nunique()) # 3
print(df.nunique()) # per column
