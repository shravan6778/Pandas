import pandas as pd
df = pd.DataFrame({
"Name": ["Amit","ravi","SURESH"],
"Salary": [30000, 35000, 42000],
"Score": [78, 82, 85]
})
# .map() — element-wise on a SINGLE SERIES 
# Perfect for simple value substitutions
df["Name_Upper"] = df["Name"].map(str.upper)
df["Grade"] = df["Score"].map({78:"C", 82:"B", 85:"B"})
# map with a lambda
df["Salary_K"] = df["Salary"].map(lambda x: f"{x/1000:.1f}K")
print(df)

# .apply() on a SERIES — element-wise with custom logic
def categorise(score):
    if score >= 90: return "Excellent"
    elif score >= 80: return "Good"
    else: return "Average"
df["Category"] = df["Score"].apply(categorise)
print(df)
# .apply() on a DATAFRAME — across rows or columns 
# axis=0 (default) function applied to each COLUMN as a Series
# axis=1 function applied to each ROW as a Series
col_max = df[["Salary","Score"]].apply(max, axis=0) # max of each col
row_sum = df[["Salary","Score"]].apply(sum, axis=1) # sum of each row

#Custom row-level function
def annual_salary(row):
    return row["Salary"] * 12
df["Annual"] = df.apply(annual_salary, axis=1)
# Lambda shorthand
df["Annual"] = df.apply(lambda row: row["Salary"] * 12, axis=1)
print(df)