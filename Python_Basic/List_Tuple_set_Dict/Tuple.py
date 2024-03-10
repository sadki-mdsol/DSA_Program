tup = (12,14,12,16) #value can't be changed

(a1,b1,*c1) = tup

print(a1,b1,c1)
print(tup[-1])
print(tup[0])

print(tup.index(14))

print(tup.count(12)) #return count of that element in the tuple

