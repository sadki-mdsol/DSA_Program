import pandas as pd

my_dict = {
    "Calories" : [400,420,450],
    "Days" : ['Day1','Day2','Day3']
}


my_df = pd.DataFrame(my_dict)
print(my_df)


print("---------------------------------")
print(my_df.loc[0])
print(my_df.loc[[0]])

data = {
    'Name': ['Sneha','Sheetal','Shweta'],
    'Subjects' : ['Computer','IT','Civil']
}

index_number = ['D1','D2','D3']

my_df_daughter = pd.DataFrame(data , index = index_number)
print("---------------------------------")
print(my_df_daughter)
print(my_df_daughter.loc['D1'])  ## return series
print(my_df_daughter.loc[['D1']])  ## return Dataframe