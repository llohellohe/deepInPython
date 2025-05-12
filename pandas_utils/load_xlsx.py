import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name=['Sheet1', 'sheet2'])
print(df)

excel_file = pd.ExcelFile('data.xlsx')
print(excel_file.sheet_names)
print("EXCEL FILE")
df2 = excel_file.parse('Sheet1')
print(df2)
