import pandas as pd

lst = [[1,15],[2,11],[3,11],[4,20]]
df = pd.DataFrame(lst,columns = ['student_id','age'])
print(df)

print(len(df.axes[0]))

print(len(df))
print(len(df.columns))

print(df.shape)