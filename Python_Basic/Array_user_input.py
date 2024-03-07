from array import *

arr =array('i',[])

len = int(input("Enter number of element: "))


for i in range(len):
    arr.append(int(input("Enter the value")))

print(arr)

search = int(input("Enter Search Element"))

index =0 
for i in arr:
    if i== search:
        print("Element Present",index)
        break
    index+=1

print(arr.index(search))