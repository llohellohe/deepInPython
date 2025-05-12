import pandas as pd

df = pd.read_csv('nba.csv')
print(df.to_string())

df.to_csv('/tmp/nba-1.csv')

