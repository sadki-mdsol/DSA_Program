from array import *

val = array('i',[10,20,30,100])

new_arr = array(val.typecode,(a for a in val ))

print(new_arr)
print(val)

print(val.index(10))

print(val.buffer_info())

print(val[0])

for i in range(4):
    print(val[i])

print("-----")

for i in range(len(val)):
    print(val[i])

print("-----")
for e in val:
    print(e)

# charachetr
chr = array('u',['a','b','i'])

print(chr)
for e in chr:
    print(e)