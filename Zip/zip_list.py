names = ('Sneha','Vijay','Sheetal','Sneha')
cmpy =('DS','Apple','ios','DS')

print("zip via list------------------------")
zipped_result = list(zip(names,cmpy))
print(zipped_result)

print("zip via set------------------------")
zipped_result = set(zip(names,cmpy))
print(zipped_result)

print("zip via dict------------------------")
zipped_result = dict(zip(names,cmpy))
print(zipped_result)


print("Via for loop-----------------")

for (a,b) in zip(names,cmpy):
    print(a,b)