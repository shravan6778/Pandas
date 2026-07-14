import pandas as pd
df = pd.DataFrame({
"OrderDate": ["2026-07-11", "2026-07-12", "2026-07-13", "2026-07-14",
"2024-02-14","2024-03-05","2024-06-21"],
"Sales": [1500, 2200, 3100, 1800, 2500, 2900, 3400]
})
# Convert string to datetime 
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
# Extract components using .dt accessor 
df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month # 1-12
df["Day"] = df["OrderDate"].dt.day
df["Quarter"] = df["OrderDate"].dt.quarter # 1-4
df["DayName"] = df["OrderDate"].dt.day_name() # 'Monday'...
df["MonthName"]= df["OrderDate"].dt.month_name() # 'January'...
df["DayOfWeek"]= df["OrderDate"].dt.dayofweek # 0=Mon ... 6=Sun
df["IsWeekend"]= df["OrderDate"].dt.dayofweek >= 5
df["WeekNum"] = df["OrderDate"].dt.isocalendar().week
# Date arithmetic 
from datetime import datetime
today = pd.Timestamp("today")
df["Days_Since"] = (today - df["OrderDate"]).dt.days
df["Future_Date"] = df["OrderDate"] + pd.DateOffset(months=3)
# Set datetime as index for time-series operations 
df = df.set_index("OrderDate")
# Resample — aggregate by time period 
# Collapse all orders by MONTH and sum sales
monthly = df["Sales"].resample("ME").sum() # 'ME' = Month End
# Or: 'W'=week, 'QE'=quarter end, 'YE'=year end, 'D'=day
# For older Pandas: 'M', 'Q', 'Y'
print(monthly)
# OrderDate
# 2023-01-31 4600
# 2023-03-31 2200 ...
# Rolling window
df["Sales_7d_avg"] = df["Sales"].rolling(window=7).mean()
# Filtering by date 
df.loc["2023-01":"2023-06"] # Jan–Jun 2023 (partial string slicing)
df.loc["2024"] # whole year 2024