def even_odd_count(list):
    even =0
    odd =0
    for x in list:
        if x%2 ==0:
            even+=1
        else:
            odd+=1

    return even,odd


even ,odd =even_odd_count([10,2,11,13,15,16,20])

print("Even ",even)
print("Odd ",odd)

print("even : {} \nOdd : {}".format(even,odd))
