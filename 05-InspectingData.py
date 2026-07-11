import pandas as pd
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# Preview 
df.head(10) # first 10 rows (default 5)
df.tail(10) # last 10 rows
# Structure 
print(df.shape) # (2823, 25) fi 2823 rows, 25 columns
print(df.columns) # list all column names
# Index(['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', ...])

print(df.dtypes) # data type per column
# ORDERNUMBER int64
# QUANTITYORDERED int64
# PRICEEACH float64 ...

# info() — the most useful single command 
df.info()

# nn describe() — statistics for numeric columns nnnnnnnnnnnnnnn
df.describe()
# Returns: count, mean, std, min, 25%, 50% (median), 75%, max
# Include object (string) columns too
df.describe(include="all")
df.describe(include="object") # just text columns
# nn Accessing a single column nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
print(df["ORDERNUMBER"]) # Series
print(df[["ORDERNUMBER","QUANTITYORDERED"]]) # DataFrame