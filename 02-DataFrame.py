import pandas as pd
# Create from a dictionary ‹ most common in practice
data = {
"Name": ["Amit", "Ravi", "Suresh", "Kiran", "Anjali"],
"Age": [22, 25, 28, 30, 24],
"Salary": [30000, 35000, 42000, 50000, 38000],
"Score": [78, 82, 85, 90, 80]
}
df = pd.DataFrame(data)
print(df)
# Create from a list of dicts
rows = [{"Name": "Pooja", "Age": 26}, {"Name": "Rahul", "Age": 29}]
df2 = pd.DataFrame(rows)
# Key attributes
print(df.shape) # (5, 4) fi rows, columns
print(df.columns) # Index(['Name', 'Age', 'Salary', 'Score'])
print(df.index) # RangeIndex(start=0, stop=5, step=1)
print(df.dtypes) # data type of each column
print(df.values) # 2-D numpy array
# Select a single column fi returns a Series
print(df["Name"])
# Select multiple columns fi returns a DataFrame
print(df[["Name", "Salary"]])
# Add a new column (vectorised)
df["Bonus"] = df["Salary"] * 0.10
df.insert(0, "EmpID", range(100, 105)) # insert at specific position insert(loc,colname,values)
# Update a cell: df.loc[row_label, col_name] = value
df.loc[0, "Salary"] = 35000
# Update entire column
df["Salary"] = df["Salary"] * 1.05 # 5% hike for everyone
# Drop a column
df.drop(columns=["Bonus"], inplace=True)
