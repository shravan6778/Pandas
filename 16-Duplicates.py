import pandas as pd
df = pd.DataFrame({
"EmpID": [101, 102, 101, 103, 102, 104],
"Name": ["Amit","Ravi","Amit","Kiran","Ravi","Anjali"],
"Dept": ["IT","HR","IT","Finance","HR","IT"]
})
# duplicated() — returns boolean mask 
print(df.duplicated())

# Count duplicates
print(df.duplicated().sum()) # 2
# Mark first occurrence as duplicate (keep='last')
df.duplicated(keep="last") # marks EARLIER ones as True
# Mark ALL occurrences as duplicate
df.duplicated(keep=False)
# Check duplicates on specific columns only
df.duplicated(subset=["EmpID"])
df.duplicated(subset=["Name","Dept"])
# drop_duplicates() — remove them 
clean = df.drop_duplicates() # remove all dups, keep first
clean = df.drop_duplicates(keep="last") # keep last occurrence
clean = df.drop_duplicates(subset=["EmpID"]) # only check EmpID
clean = df.drop_duplicates(subset=["EmpID"], keep="first", inplace=False)
df.drop_duplicates(inplace=True) # modify in place