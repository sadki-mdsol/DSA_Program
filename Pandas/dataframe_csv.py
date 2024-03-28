import pandas as pd

df = pd.read_csv('data.csv.txt')

print(df)
print(df.to_string())
print("Maximum rows the df should return",pd.options.display.max_rows)

pd.options.display.max_rows = 100
print(df)
print("Maximum rows the df should return",pd.options.display.max_rows)