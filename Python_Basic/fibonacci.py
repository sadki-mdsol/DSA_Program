def fibonacci(end):
    a=0
    b= 1
    print(" {} {} ".format(a,b),end="")
    while end >b:
        s = a + b
        a = b
        b = s
        print(" {} ".format(s),end="" if end >b else None)



end = int(input("Enter number till which series should end"))
fibonacci(end)