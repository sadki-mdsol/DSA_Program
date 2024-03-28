import pandas as pd 

arr = [2,6,7,8]

mydataframe = pd.Series(arr)
print(mydataframe)

print(mydataframe[0])

my_label_df = pd.Series(arr,index=['L1','L2','L3','L3'])

print(my_label_df)

print(my_label_df['L3'])

# key/value to dict

cal = {'Day1':80,'Day2':100,'Day3':60}

mydictdf = pd.Series(cal)

print(mydictdf)
print(mydictdf['Day1'])

print(mydictdf.size)