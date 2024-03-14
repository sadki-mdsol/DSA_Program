import mysql.connector

mybd = mysql.connector.connect(host='localhost',user='sneha',passwd='Vijay@1996',database ='Telusko')

mycursor = mybd.cursor()


db_names = mycursor.execute("show databases")

all_data = mycursor.execute("select * from Student")

for i in all_data:
    print(i)

result_all= mycursor.fetchall()

result_one= mycursor.fetchone()

