arr = [10,3,6,2,9]
search_ele = 9
pos = -1

for i in arr:
    pos = pos+1
    if i==search_ele:
        print("Element Present {} ".format(pos))
        break

else:
    print("Element not present")