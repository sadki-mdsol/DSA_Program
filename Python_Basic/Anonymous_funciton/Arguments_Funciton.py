def update(x):
    print(id(x))
    x=100
    print(x)
    print(id(x))


a = 5
print(id(a))
update(a)
print(a)


print("via list---------")
def update_lst(lst1):
    print(id(lst1))
    lst1[0]=100
    print(id(lst1))
    print(lst1)


lst = [10,20,30]
print(id(lst))
update_lst(lst)
print(id(lst))
print(lst)