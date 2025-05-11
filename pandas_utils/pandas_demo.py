import pandas as pd

data = {'Name': ['G1', 'G2', 'G3'], 'Age': [1, 2, 3]}

df = pd.DataFrame(data)

print(df)

# 创建两个Series对象
series_apples = pd.Series([1, 3, 7, 4])
series_bananas = pd.Series([2, 6, 3, 5])

df = pd.DataFrame({'N1': series_apples, 'N2': series_bananas})
print(df)

print("=" * 6 + " Series " + "=" * 6)
column1 = pd.Series([1, 2, 3], name='C1')
print(column1)

d = ['a', 'b', 'c']
column2 = pd.Series(d, name='C2', index=['a1', 'a2', 'a3'])
print(column2)
print(column2['a2'])

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
column3 = pd.Series(sites)
print(column3)

column4 = pd.Series(sites, index=[1, 3], name='PART')
print(column4)

print(column1.head(2))
print(column1.tail(2))
print(column1.shape)

column4.map(print)
print("APPLY")
print(column1.apply(lambda x: x * 2))
print(column1)
column1.apply(lambda x: x * 2)

column5 = pd.Series([1, 2, 3, None, 4, 2])
print(column5)
column5.fillna("FILL")
print(column5)
column5.fillna(value=0)
# print(column5.fillna(value='FILL'))
column5 = column5.dropna()
print(column5)

column5[0] = 11
del column5[5]
print(column5)

print("SUM IS")
print(column5.sum)
print(column5.dtype)

print(column5.astype(int))
print(column5.dtype)

print("==DATA FRAME==")

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

df = pd.DataFrame(data, columns=['Site', 'Age'])

print(df)
print("Age type")
print(df['Age'].dtype)
print(df['Age'].astype(str))
df['Age'] = df['Age'].astype(str)
print(df['Age'].dtype)
print("===")
print(df['Age'].dtype)
# print(df['Age'].astype(str))
