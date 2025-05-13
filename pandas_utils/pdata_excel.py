import pandas as pd

df = pd.read_csv('pdata.csv')
print(df)
print("=====")
# print(df.dropna(inplace=True))
print("=====AFTER DROP=====")
print(df)

print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())

print(df.dropna(subset=['ST_NUM']))
print(df['ST_NUM'].fillna('AA'))
