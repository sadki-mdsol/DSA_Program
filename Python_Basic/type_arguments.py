#variable Length
print("Variable Lenght---------")
def add(*b):
    c=0
    for i in b:
        c= c+i
    print(c)


add(10)
add(10,20,30)

print("Position---------")

def person(name,age):
    print(name,age-5)

person("sneha",10)
# person(10,"Sneha" )#this will throw error becz position matter

#keyword 
print("Keyword type---------")
person(age=50,name='Vijay')

# default
print("Default Tyep---------")
def openAccount(name,age=10):
    print(name,age)

openAccount("Sneha",30)
openAccount("Vijay")


def persion(name,**data):
    print(name)
    for k,v in data.items():
        print(k,"-->",v)

persion("Sneha",age='30',city='Mumbai',m_no=98765)