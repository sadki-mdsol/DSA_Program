from numpy import *

# for above scenario both array have same address and samme value pointing to
print("Copy------------------------")
arr1 = array([2,6,8,1])
arr2 =arr1

print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)

arr1[0] = 10
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)

#shallow Copy (view)
#here both have different address but the value is getting update if we chaneg in another array

print("Shallow Copy------------------------")
arr3 = array([2,6,8,1])
arr4 = arr3.view()

print(id(arr3))
print(id(arr4))
print(arr3)
print(arr4)

arr3[3]= 10

print(id(arr3))
print(id(arr4))
print(arr3)
print(arr4)

# deep copy copy()
# here the value are not linked & also adress
print("Deep Copy------------------------")

arr5 = array([3,4,5,6])
arr6 =arr5.copy()

print(id(arr5))
print(id(arr6))
print(arr5)
print(arr6)

arr5[0] = 100
print(id(arr5))
print(id(arr6))
print(arr5)
print(arr6)