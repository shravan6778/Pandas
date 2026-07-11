import pandas as pd
df = pd.DataFrame({
"Name": ["Amit","Ravi","Suresh","Kiran","Anjali","Pooja"],
"Age": [22, 25, 28, 30, 24, 26],
"Salary": [30000, 35000, 42000, 50000, 38000, 45000],
"Score": [78, 82, 85, 90, 80, 88],
"Dept": ["IT","HR","Finance","IT","HR","IT"]
})
# Single condition 
print(df[df["Salary"] > 40000])
# AND (&) — both conditions must be True 
print(df[(df["Salary"] > 35000) & (df["Age"] > 25)])
# OR (|) — at least one condition must be True 
print(df[(df["Age"] > 30) | (df["Score"] > 88)])
# NOT (~) — invert a condition 
print(df[~(df["Dept"] == "HR")]) # everyone NOT in HR
# .isin() — match any value in a list 
print(df[df["Dept"].isin(["IT", "Finance"])])
# .between() — range check (inclusive) 
print(df[df["Salary"].between(35000, 50000)])
# .query() — cleaner SQL-like syntax 
print(df.query("Salary > 40000 and Age > 25"))
print(df.query("Dept == 'IT' or Score > 88"))
print(df.query("Salary.between(35000, 50000)"))
# Reference Python variables inside query with @
min_sal = 40000
print(df.query("Salary > @min_sal"))
