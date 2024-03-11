a = 10
b = 2

try:
    print("Resource opened")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Exception occured for ZeroDivisionError {}".format(e))
except ValueError as e:
    print("Exception occured for ValueError {}".format(e))
except Exception as ex:
    print("Exception Occured {}".format(ex))
finally:
    print("Resource Closed")
