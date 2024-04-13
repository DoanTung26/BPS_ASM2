import pandas as pd
df = pd.read_excel("tungdoan.xlsx", sheet_name="Sheet1")
index_to_drop = 3
df.drop(index_to_drop, inplace=True)
print(df)
