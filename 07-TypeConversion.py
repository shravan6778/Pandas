import pandas as pd
df = pd.DataFrame({
"EmpID": ["101", "102", "103"],
"Age": ["22", "25", "28"],
"Salary": ["30000.5", "35000", "42000.75"],
"Joined": ["2022-01-15", "2021-06-01", "2023-03-10"],
"IsActive": ["True", "False", "True"]
})
print(df.dtypes) # everything is 'object' (string)
# astype() — direct cast 
df["EmpID"] = df["EmpID"].astype(int)
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)
df["IsActive"] = df["IsActive"].astype(bool)
# Cast multiple at once
df = df.astype({"EmpID": int, "Age": int, "Salary": float})
# nn pd.to_numeric() — safe numeric conversion 
# errors='coerce' fi converts bad values to NaN instead of crashing
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
# pd.to_datetime() — parse date strings 
df["Joined"] = pd.to_datetime(df["Joined"])
print(df["Joined"].dtype) # datetime64[ns]
# Custom format
df["Joined"] = pd.to_datetime(df["Joined"], format="%Y-%m-%d")
# After conversion, extract parts
df["Year"] = df["Joined"].dt.year
df["Month"] = df["Joined"].dt.month
df["Day"] = df["Joined"].dt.day
df["DayName"] = df["Joined"].dt.day_name() # 'Monday', 'Tuesday' ...
print(df.dtypes)