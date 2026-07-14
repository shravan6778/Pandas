import pandas as pd
import numpy as np
df = pd.DataFrame({
"Name": ["Amit","Ravi","Suresh","Kiran","Anjali","Pooja"],
"Dept": ["IT","HR","Finance","IT","HR","IT"],
"Region": ["South","North","South","North","South","North"],
"Salary": [30000,35000,42000,50000,38000,45000],
"Score": [78,82,85,90,80,88]
})
# pivot_table() 
# Parameters: values, index, columns, aggfunc, fill_value, margins
pivot = pd.pivot_table(
df,
values="Salary", # values to aggregate
index="Dept", # rows
columns="Region", # columns
aggfunc="sum", # function: mean/sum/count/max/min/np.sum, default=mean, for multiple: aggfunc=['sum','mean']
fill_value=0, # fill NaN with 0
margins=True # add Row/Column totals (Grand Total row)
)
print(pivot)

# pd.crosstab() — frequency counts 
# Like pivot but counts occurrences (no separate 'values' column needed)
ct = pd.crosstab(df["Dept"], df["Region"])
print(ct)

# With normalize (proportions instead of counts)
ct_norm = pd.crosstab(df["Dept"], df["Region"], normalize="index")
# Each row sums to 1.0 (proportions within dept)
print(ct_norm)

# Crosstab with aggregation
ct_sal = pd.crosstab(df["Dept"], df["Region"],
values=df["Salary"], aggfunc="mean")
print(ct_sal)