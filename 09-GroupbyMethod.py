import pandas as pd
df = pd.DataFrame({
"Name": ["Amit","Ravi","Suresh","Kiran","Anjali","Pooja","Rahul"],
"Dept": ["IT","HR","Finance","IT","HR","IT","Finance"],
"Age": [22, 25, 28, 30, 24, 26, 29],
"Salary": [30000,35000,42000,50000,38000,45000,52000],
"Score": [78,82,85,90,80,88,92]
})

# Basic groupby + single agg 
dept_salary = df.groupby("Dept")["Salary"].sum()
print(dept_salary)

df.groupby("Dept")["Salary"].mean()

# .agg() — multiple aggregations at once 
result = df.groupby("Dept")["Salary"].agg(["mean","sum","max","min","count"])
print(result)
# Named aggregations (clean column names)
result = df.groupby("Dept").agg(
avg_salary=("Salary", "mean"),
total_salary=("Salary", "sum"),
avg_score=("Score", "mean"),
headcount=("Name", "count")
)
print(result)

# Multi-column groupby 
df.groupby(["Dept","Age"])["Salary"].sum()

# .transform() — adds result back as a column (same length!)
df["Dept_Avg_Salary"] = df.groupby("Dept")["Salary"].transform("mean")

# Now each row has the department average — useful for feature engineering!
# e.g., salary_vs_dept_avg = df["Salary"] - df["Dept_Avg_Salary"]
# .apply() — full custom function per group 
def top_earner(group):
    return group.nlargest(1, "Salary")
top_per_dept = df.groupby("Dept").apply(top_earner)
print(top_per_dept)
# .filter() — keep only groups meeting a condition 
big_depts = df.groupby("Dept").filter(lambda g: len(g) >= 2)
