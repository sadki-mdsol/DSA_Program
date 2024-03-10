def fibonacci(end):
    if end >0:
        a=0
        b= 1
        print(" {} {} ".format(a,b),end="" if end >b else None)
        while end >b:
            s = a + b
            a = b
            b = s
            print(" {} ".format(s),end="" if end >b else None)
    else:
        print(" Can't print Fibonacci")



end = int(input("Enter number till which series should end"))
fibonacci(end)