from numpy import *

#array()

arr1 = array([10,20,30])

print(arr1)

arr2 = array([10,20,30.0])

print(arr2) #default typecast into to float

arr3 = array([10,20,30.0],'int') #it will convert all element to int
print(arr3)



#linspace(stat nu,end numincluded , no of parts)

arr4 = linspace(1,10,5)

print(arr4)


#arange(start number,end number excluded,total count to skip)

arr5 = arange(1,20)

print(arr5)


#logspace(s_in, end_index,div) log to the base starts from s_in till end_index & divides by div
arr6 = logspace(1,50,5)

print(arr6)


#zeros(sixe array) & ones(array_size,int,flaot) default is float in o/p if we specify the int

arr7= zeros(6,int)
print(arr7)

arr8= zeros(6)
print(arr8)