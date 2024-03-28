import pandas as pd

mydataset = {
  'student_id': [101,53,128,3],
  'name': ['Ulysses','William','Henry','Henry'],
  'age' : [13,10,6,11]
}

my_df = pd.DataFrame(mydataset)
print(my_df)
print(my_df.loc[my_df['student_id']== 101, ['name', 'age']])

print(my_df[my_df['student_id']==101][['name',"age"]])


# | student_id | name    | age |
# | ---------- | ------- | --- |
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |