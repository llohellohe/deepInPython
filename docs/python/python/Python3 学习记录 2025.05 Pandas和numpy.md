
详细教程：https://www.runoob.com/pandas/pandas-series.html

# Series
1.pandas 中的一个重要数据结构----Series
相当于是一列。

```
d = ['a', 'b', 'c']  
column2 = pd.Series(d, name='C2',index=['a1','a2','a3'])  
print(column2)  
print(column2['a2'])
```

2.可以设置index值，设置后按照设置的index去读取。如上中的'a2'。

```
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}  
column3 = pd.Series(sites)  
print(column3)  
  
column4 = pd.Series(sites, index=[1, 3], name='PART')  
print(column4)
```

3.Series初始化时，可以指定部分index数据

```
column5 = pd.Series([1, 2, 3, None, 4, 2])  
print(column5)  
print(column5.dropna())
```
* dropna,去除空值。但是不修改Series本身。
* fillna，填充值。但是不修改Series本身。

```
column5[0]=11  
del column5[5]  
print(column5)
```

4.赋值和删除操作，会改变 原Series
5.apply\map\astype等不会改变 原Series

# DataFrame
pandas中的另一个核心数据结构，类似于二维的表格。
* 每一列都是一个Series


1. descripe() 返回数值列的统计信息，比如值、标准差、最小值等
2. shape()返回行数、列数，比如5行2列（5，2）
3. sort_values('Champion', ascending=False)
	1. ascending  升序、上升的；False代表是降序，即从大到小。
4. dropna()删除行或者列包含 NaN的。原df不影响。
5. loc[]按照标签索引
6. iloc[]按照位置索引
7. at和iat类似上面，可以按照行列取单个元素，比上面更加高效
```
print(df.at[0, 'Champion'])  
print(df.iat[0, 0])
```
参考代码：https://blog.csdn.net/W_weiying/article/details/84787423
8. to_csv to_json
9. drop_duplicates 删除重复行
10. duplicated()重复项https://blog.csdn.net/u014740628/article/details/134047456
11. 纵向、横向合并
```
# 纵向合并
pd.concat([df1, df2], ignore_index=True)

# 横向合并
pd.merge(df1, df2, on='Column1')
```
12. filter 根据大小来做筛选 print(dfab[dfab['Champion'] > 2])

## set_index reset_index
参考文档：https://blog.csdn.net/jingyi130705008/article/details/78162758


## loc切片
```
print("单个label切片")  
print(dfab.loc[1:2, 'Team_x'])  # 标签索引提取指定行列

#单个label切片
#1    LAL
#2    HOU
```

和普通切片不同的是，起、始位置都包含。
https://blog.csdn.net/brucewong0516/article/details/82494090


## 数据透视
pivot，长格式转宽格式，实现数据透视功能 https://blog.csdn.net/cxd3341/article/details/105016903
melt，宽数据变长数据 https://blog.csdn.net/maymay_/article/details/80039677
```
# 长格式转宽格式
df_pivot = df.pivot(index='Column1', columns='Column2', values='Column3')

# 宽格式转长格式
df_melt = df.melt(id_vars='Column1', value_vars=['Column2', 'Column3'])
```


## read_csv
![[Pasted image 20250512205518.png]]

## read_excel
可以指定sheetname读取
```
import pandas as pd  
  
df = pd.read_excel('data.xlsx', sheet_name=['Sheet1', 'sheet2'])  
print(df)
```

### excel_file = pd.ExcelFile('data.xlsx')
把内容读取到excel中


# numpy
##  linalg 模块
https://blog.csdn.net/qq_41800366/article/details/88064717
###  范数
https://blog.csdn.net/lanchunhui/article/details/51004387
![[Pasted image 20250512141001.png]]
默认2范数

# 数据清洗
```
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

默认情况下,dropna/fillna 返回一个新的DataFrame，不会修改源数据。
可以用两个方法：
- inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
	* 设置此参数后，就可以修改源数据。
* 重新走变量赋值

## 删除指定列的 NaN
print(df.dropna(subset=['ST_NUM']))

## 填充指定列
print(df['ST_NUM'].fillna('AA'))
不能使用subset模式

## 删除错误数据 drop函数
```
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)
#
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())
```


## filter指定列
```
# 选择指定的列  
df.filter(items=['column_name1', 'column_name2'])  
  
# 选择列名匹配正则表达式的列  
df.filter(regex='regex')
```


# sort_index()
* axis=0表示按照最左边一列的索引排序
* axis=1表示按照最上面一行的索引排序
* ascending=True，升序
* ascending=False，降序

# groupby 
![[Pasted image 20250514162011.png]]


# 绘图 plot
```
df.plot(kind='line',  
        x='Year',  
        y='Sales',  
        title='Sales over years',  
        xlabel='YEAR',  
        ylabel='SALES',  
        figsize=(12, 12)  
        )  
plt.show()
```

* x 代表横轴对应的值
* y 代表纵轴对应的值
* title代表图标名称
* xlabel 横坐标标签
* ylabel 纵坐标标签
* figsize 图片大小

也可以通过如下方式设置
```
plt.title('SALES')  
plt.xlabel('Year')  
plt.ylabel('Sales')  
plt.grid(True)
```



# seaborn提供更加漂亮的图
```
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}  
df = pd.DataFrame(data)  
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')  
plt.show()
```

cmap参数可以指定不同的调色板
![[Pasted image 20250515204158.png]]

调色板详情：https://blog.csdn.net/sgzqc/article/details/137977342