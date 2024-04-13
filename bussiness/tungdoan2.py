import pandas as pd
df = pd.read_excel("tungdoan.xlsx",sheet_name="Sheet1")
pd.set_option('display.max_rows', 107)
df= df.dropna() 
print(df)