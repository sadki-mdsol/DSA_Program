def factorial(num):
    fac = 1
    str12 = ''
    for i in range(num,1,-1):
        str12 = str12 + str(i) + '*'
        fac = fac * i
    print(f"{fac}: {str12}+1")


number = int(input("Enter number of which you want to find factorial"))

factorial(number)