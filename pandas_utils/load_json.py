import pandas as pd

# JSON 数据
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''

df = pd.read_json(json_data)
print(df)

#URL = 'https://static.jyshare.com/download/sites.json'
#df = pd.read_json(URL)
#print(df)
