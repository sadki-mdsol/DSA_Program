# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+


import pandas as pd
dict_value = {
    "name" :['Piper','Grace','Georgia','Willow','Finn','Thomas','Thomas'],
    "salary":[4548,28150,1103,6593,74576,24433,24433]
}


my_df = pd.DataFrame(dict_value)

bonus = []
sqr = (lambda x: x+x)
for x in my_df['salary']:
    bonus.append(sqr(x))
my_df.insert(2,'bonus',bonus)

# print(my_df)

# print(my_df.drop_duplicates(inplace=True))
# print(my_df)


# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 5           | Finn    | john@example.com    |
# | 6           | Violet  | alice@example.com 


my_customer = {
    "customer_id": [1,2,3,4,5,6],
    "name" : ['Ella','David','Zachary','Alice','Finn','Violet'],
    "email" : ['emily@exm.com','micheal@exm.com','sarah@exm.com','john@exm.com','john@exm.com','alice@exm.com']

}


my_cus_df = pd.DataFrame(my_customer)
print(my_cus_df)

my_cus_df.drop_duplicates(subset=['email'],keep='first',inplace=True,ignore_index=False)
print(my_cus_df)


# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 217        | None    | 19  |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |

my_stud = {
    'student_id' :[32,217,779,849],
    'name':['Piper',None,'Georgia','Willow'],
    'age':[5,19,20,24]
}

my_stud_df= pd.DataFrame(my_stud)

my_stud_df.dropna(subset=['name'],inplace=True)

print(my_stud_df)


# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# +---------+--------+

my_emp = {
    'name':['Jack','Piper','Mia','Ulysses'],
    'salary' : [19666,74754,62509,54866]
}

my_emp_df = pd.DataFrame(my_emp)

print(my_emp_df)

double_sal = []
for x in my_emp_df['salary']:
    double_sal.append(x+x)

my_emp_df.replace({'salary':double_sal},inplace=True)

print(my_emp_df)