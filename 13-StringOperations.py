import pandas as pd
df = pd.DataFrame({
"Name": [" Amit Sharma ", "ravi kumar", "SURESH RAO", "kiran.nair"],
"Email": ["amit@gmail.com","ravi@yahoo.com","suresh@gmail.com","kiran@outlook.com"],
"Phone": ["9876543210", "8765432109", "7654321098", "6543210987"],
"City": ["Hyderabad, Telangana", "Mumbai, Maharashtra",
"Bangalore, Karnataka", "Chennai, Tamil Nadu"]
})
# Case 
print(df["Name"].str.upper())
print(df["Name"].str.lower())
print(df["Name"].str.title())

# Strip whitespace
print(df["Name"].str.strip()) # both ends
print(df["Name"].str.lstrip()) # left only
print(df["Name"].str.rstrip()) # right only

# Contains / Startswith / Endswith 
df[df["Email"].str.contains("gmail")] # rows with gmail
df[df["Email"].str.endswith(".com")]
df[df["Name"].str.startswith("A")]
# na=False avoids errors on NaN values
df[df["Name"].str.contains("kumar", case=False, na=False)]

# Replace 
df["Name"] = df["Name"].str.replace(".", " ", regex=False)
# regex=True to use patterns
df["Phone"] = df["Phone"].str.replace(r"\D", "", regex=True) # digits only

print(df)

#Split 
# Split email into username and domain
split_df = df["Email"].str.split("@", expand=True)
df["Username"] = split_df[0]
df["Domain"] = split_df[1]

#Split city/state
city_state = df["City"].str.split(", ", expand=True)
df["City_Only"] = city_state[0]
df["State"] = city_state[1]

# Extract with regex
# Extract first 4 digits of phone
df["Area"] = df["Phone"].str.extract(r"(\d{4})")
# Length / Count 
df["Name"].str.len()
df["Email"].str.count("@") # how many @ in each email
# Pad / Zfill 
df["Phone"].str.zfill(10) # pad with zeros to length 10
