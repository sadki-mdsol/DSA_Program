def romanToInt(s: str):
    dict ={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }

    sum = 0
    for index,val in enumerate(s):
        if val == 'I' and index!= len(s)-1 and s[index+1] =='V':
            sum = sum - dict[val]
        else:
            sum = sum + dict[val]
        

    return sum

print(romanToInt("MCMXCIV"))
