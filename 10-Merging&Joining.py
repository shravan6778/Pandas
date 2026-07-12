import pandas as pd
df_emp = pd.DataFrame({
"EmpID": [101,102,103,104,105],
"Name": ["Amit","Ravi","Suresh","Kiran","Anjali"],
"Dept": ["IT","HR","Finance","IT","HR"]
})
df_sal = pd.DataFrame({
"EmpID": [103,104,105,106,107],
"Salary": [50000,55000,48000,60000,62000],
"Score": [88,90,85,92,91]
})
# INNER JOIN — only matching EmpIDs (103,104,105)
inner = pd.merge(df_emp, df_sal, on="EmpID", how="inner")
# LEFT JOIN — all from df_emp, NaN where no match in df_sal
left = pd.merge(df_emp, df_sal, on="EmpID", how="left")
# RIGHT JOIN — all from df_sal, NaN where no match in df_emp
right = pd.merge(df_emp, df_sal, on="EmpID", how="right")
# OUTER JOIN — all rows from both, NaN where no match
outer = pd.merge(df_emp, df_sal, on="EmpID", how="outer")
# CROSS JOIN — every row with every row (no key needed)
cross = pd.merge(df_emp, df_sal, how="cross")

df_employees = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Ravi", "Suresh", "Kiran", "Anjali"],
    "Age": [25, 28, 30, 27, 24],
    "Department": ["IT", "HR", "Finance", "IT", "HR"]
})

df_salary = pd.DataFrame({
    "EmpID": [103, 104, 105, 106, 107],
    "Salary": [50000, 55000, 48000, 60000, 62000],
    "PerformanceScore": [88, 90, 85, 92, 91]
})

print(df_employees)
print(df_salary)

#Row-wise Concatenation
pd.concat([df_employees, df_employees], ignore_index=True)

#Column-wise Concatenation
pd.concat([df_employees, df_salary], axis=1, ignore_index=True)
