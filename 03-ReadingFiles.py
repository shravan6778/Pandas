import pandas as pd
from sqlalchemy import create_engine
# CSV 
df_csv = pd.read_csv("sales_data.csv", encoding="latin1")
# Useful parameters:
# sep=',' fi delimiter (default comma; use '\t' for TSV)
# encoding='utf-8' fi 'latin1' fixes "UnicodeDecodeError" on messy files
# header=0 fi row to use as column names (0 = first row)
# index_col=None fi column to use as the row index
# usecols=['A','B']fi load only specific columns (saves memory)
# nrows=1000 fi load only first N rows
# na_values=['NA','--'] fi treat extra strings as NaN

#  Excel 
df_xl = pd.read_excel("SampleSuperstore.xlsx", sheet_name=0)
# sheet_name='Sheet1' or 0 (int index), or list for multiple sheets

#  JSON 
df_json = pd.read_json("data.json")
# orient='records' fi list of dicts | 'index' fi nested dict

#  SQL 
engine = create_engine("mysql+pymysql://root:pass@localhost:3306/mydb")
df_sql = pd.read_sql("SELECT * FROM users", con=engine)
df_sql2 = pd.read_sql_table("users", con=engine) # entire table
df_sql3 = pd.read_sql_query("SELECT id, name FROM users WHERE age > 25",
con=engine) # just a query

#Writing Files
df={
    "Name":['Shravan','Sandy','Ceo Of India'],
    "Age":[21,20,100],
    "City":['Hyderabad','Hyd','Hyd']
}
#to_csv
df.to_csv("output.csv", index=False)
# index=False fi do NOT write the row numbers as a column (almost always want this)
# sep=',' encoding='utf-8'
#to_excel
df.to_excel("output.xlsx", sheet_name="Results", index=False)
#to_json
df.to_json("output.json", orient="records", indent=2)
#to_sql
df.to_sql("table_name", con=engine, if_exists="replace", index=False)
# if_exists: 'fail' | 'replace' | 'append'