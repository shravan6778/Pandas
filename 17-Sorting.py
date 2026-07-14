import pandas as pd
df = pd.DataFrame({
"Name": ["Amit","Ravi","Suresh","Kiran","Anjali"],
"Age": [22, 25, 28, 30, 24],
"Salary": [30000,35000,42000,50000,38000],
"Score": [78, 82, 85, 90, 80]
})
# sort_values() — sort by column values 
# Ascending (default)
df.sort_values(by="Age", ascending=True, inplace=True)
# Descending
df.sort_values(by="Salary", ascending=False, inplace=True)
# Sort by MULTIPLE columns
# Primary: Age ascending, Secondary: Salary descending
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
# Handle NaN: put at beginning or end
df.sort_values(by="Score", na_position="last") # NaN at bottom
df.sort_values(by="Score", na_position="first") # NaN at top

# sort_index() — sort by row index 
df.sort_index(ascending=True, inplace=True) # restore original order
df.sort_index(ascending=False) # reverse index
# Sort by column INDEX (sort columns alphabetically)
df.sort_index(axis=1)

# nlargest() / nsmallest() — top/bottom N rows 
top_5 = df.nlargest(5, "Salary") # top 5 salaries
bottom_3 = df.nsmallest(3, "Age") # 3 youngest employees