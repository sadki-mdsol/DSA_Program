def Atoi(str):
    res= ""
    for i in range(len(str)):
        if str[i] in ['0','1','2','3','-','+','4','5','6','7','8','9']:
            res= res + str[i]
        if i ==0 and str[i] not in ['0','1','2','3','-','+','4','5','6','7','8','9']:
            return 0
    return int(res)

print(Atoi("abc -42"))