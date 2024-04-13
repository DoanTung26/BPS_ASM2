import pandas as pd
df = pd.read_excel("tungdoan.xlsx", sheet_name="Sheet1")
df.drop(columns=['UserID'], inplace=True)
print(df)
