import pandas as pd
# Create from a list (default integer index)
s1 = pd.Series([10, 20, 30, 40])
print(s1)
# 0 10
# 1 20 ...
# Create with custom index
s2 = pd.Series([85, 92, 78], index=["Maths", "Science", "English"])
print(s2["Maths"]) # 85
# Create from a dictionary
s3 = pd.Series({"Hyderabad": 10_000_000, "Mumbai": 20_000_000})
# Key attributes
print(s2.values) # numpy array: [85 92 78]
print(s2.index) # Index(['Maths', 'Science', 'English'])
print(s2.dtype) # int64
print(s2.shape) # (3,)
print(s2.name) # None (can be set)
# Basic operations (vectorised – no loops needed!)
print(s2 * 2) # multiply every score by 2
print(s2[s2 > 80]) # boolean filter
print(s2.mean(), s2.max(), s2.min())
