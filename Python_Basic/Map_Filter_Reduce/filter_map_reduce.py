from functools import reduce


print("Filter--------------------------------------")
number = [1,2,3,5,7,4,16]

even = list(filter(lambda x : x%2 ==0,number))

print("Even get via filter {}".format(even))

print("map()--------------------------------------")
doule_evene = list(map(lambda a:a*2,even))
print(doule_evene)

print("reduce()--------------------------------------")
sum_double_even = reduce(lambda a,b:a+b , doule_evene)
print(sum_double_even)
