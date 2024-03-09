def fact(number):
    # f = 1
    # for i in range(number,1,-1):

    if number == 1:
        return 1
    else:
        return number*fact(number-1)
        

print(fact(int(input("Enter number"))))