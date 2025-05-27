# merge
```
import pandas as pd  
  
left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})  
  
right = pd.DataFrame({'ID': [1, 2, 4], 'Age': [24, 27, 22]})  
  
print(left)  
  
print(right)  
  
result = pd.merge(left, right, on='ID')  
print(result)
```

通过merge函数，以on列来做合并；最后只有能合并的数据才会出现。如上会抛弃ID3和ID4的数据。

# concat
```
print("==CONCAT==")  
result = pd.concat([left, right], ignore_index=True)  
print(result)  
  
print("==CONCAT==AXIS=1")  
result = pd.concat([left, right], axis=1)  
print(result)  
  
print("==CONCAT==AXIS=0")  
result = pd.concat([left, right], axis=0)  
print(result)
```

代表合并的轴
axis=0，即默认值，为纵向合并。从轴来看就是横向的。
axis=1，为横向合并。从轴来看就是纵向的。

# Join
```
left = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])  
right = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 4])  
  
print(left)  
print(right)  
  
result = left.join(right, how='inner')  
print(result)
```

* left：以左边为主来连接
* right:以右边为主来连接
* outer:全链接
* inner:交集部分链接


# apply \map\applymap
对df或者series运行指定函数

# groupby
```
grouped = df.groupby('Category')['Value'].sum()
```

按照求和来分组聚合

# 时间序列操作

产生时间序列，按照时间做偏移
```
date_range = pd.date_range(start='2025-01-01', periods=5, freq='D')  
print(date_range)  
  
date = pd.to_datetime('2024-01-01')  
new_date = date + pd.Timedelta(days=10)  
print(new_date)
```