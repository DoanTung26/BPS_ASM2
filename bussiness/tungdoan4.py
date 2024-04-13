import pandas as pd
df = pd.read_excel("tungdoan.xlsx", sheet_name="Sheet1")
columns_to_drop = ['AccessID', 'UserID', 'PageVisited']
df.drop(columns=columns_to_drop, inplace=True)
print(df)
