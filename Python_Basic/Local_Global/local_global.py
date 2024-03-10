# we can access the global variable directly inside any funciton
print("we can access the global variable directly inside any funciton-----------")
a=10
def something():
    print(a)

something()
print("Outside :",a)


# if we have same name inside local & global then it's scope defines
print("if we have same name inside local & global then it's scope defines-----------")
b=10
def something_1():
    b=100
    print("inside_funciton",b)

something_1()
print("Outside :",b)

#if we use global inside any method use global keyword

print("if we use global inside any method use global keyword-----------")
c=10
print("Ouside Fucniton",id(c))
def scenario_2():
    global c
    c=45
    print("Inside Fucniton",c)
    print("Inside Fucniton",id(c))

scenario_2()
print("outside Value",c)


# if we want to have local & global same variable name

print("if we want to have local & global same variable name---------")
d=100
print("outside Address of d ",id(d))
def scenario_4():
    d = 25
    x = globals()['d']
    globals()['d'] = 100
    print("local value of d ",d)
    print("global value of d ",x)
    print("Address gloabl of d ",id(x))


scenario_4()
print("outside d value",d)

print(globals())
