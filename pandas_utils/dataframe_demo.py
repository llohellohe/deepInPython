import pandas as pd

data = {
    'Team': ['LAL', 'HOU', 'LAC', None, None, 'LAL'],
    'Champion': [2, 10, 0, None, 1, 2]
}

df = pd.DataFrame(data)

print(df.dropna())
print(df)

print(df.head(2))
print(df.tail(1))
print("INFO")
print(df.info())
print("DESCRIPTION")
print(df.describe())
print(df.shape)
print(df.columns)
print(df.index)
print(df.sort_values('Champion', ascending=False))
print(df.sort_index())
print(df.isnull)
print(df.loc[2])
print(df.iloc[2])
print(df.at[0, 'Champion'])
print(df.iat[0, 0])
print(df.duplicated())

print(df.to_csv(path_or_buf="/tmp/a.csv"))
print(df.to_json(path_or_buf="/tmp/a.json"))
print(df.to_json())
print(df)
print(df.drop_duplicates())

print("FIND DUPLICATES")
df2 = df.duplicated()
print(df.duplicated().sum)
print(df2.sum)
print("sum ", df2.sum)

print("MERGE AND CONCAT")
dfa = pd.DataFrame(data)
dfb = pd.DataFrame(data)
print(dfa)
print(dfb)

print("CONCAT")
print(pd.concat([dfa, dfb]))
print("MERGE")
print(pd.merge(dfa, dfb))
dfab = pd.merge(dfa, dfb, on='Champion')
print(dfab)

# dfab.set_index('Champion', inplace=True)
# print(dfab)

dfab.set_index('Team_x', inplace=True)
print(dfab)

dfab.reset_index(inplace=True)
print(dfab)

print("FILTER")
print(dfab[dfab['Champion'] > 2])

print("多个label切片")
print(dfab.loc[1:2, ['Team_x', 'Champion']])  # 标签索引提取指定行列

print("单个label切片")
print(dfab.loc[1:2, 'Team_x'])  # 标签索引提取指定行列

l1 = [1, 2, 3, 4]
print(l1[1:2])


print(dfab[['Team_x']])
print(dfab.loc[:, 'Team_x'])     # 提取单列

