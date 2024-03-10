# with arg with rtn value
def add_sub(v1,v2):
    return v1+v2

#without arg with return
def get_pi():
    return 3.14

#without arg without rtn
def display_not_found():
    print("Page Not Fopund")

#with arg without rtn
def gree(name):
    print(f"He {name}")

#with multiple return 
def add_sub_return(v1,v2):
    return v1+v2, v1-v2

print(add_sub(10,20))
print(get_pi())
print(display_not_found())
print(gree("Sneha"))
add,sub = add_sub_return(10,20)
print(add , sub)

