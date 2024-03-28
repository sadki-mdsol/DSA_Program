import pandas as pd

df = pd.read_json('json_file.json')

print(df)

print(df.to_string())


print('-----------head()------------')
print(df.head(2))

print(df.head())



print('-----------tail()------------')
print(df.tail(2))

print(df.tail())

print("---------info()-----------")
print(df.info())