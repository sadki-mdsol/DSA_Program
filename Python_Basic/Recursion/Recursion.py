
import sys

# by default recursion count is 1000
print(sys.getrecursionlimit())
sys.setrecursionlimit(6000)

print(sys.getrecursionlimit())

i = 0
def greet():
    globals()['i'] +=1
    print("Hello {}".format(globals()['i']))
    greet()


greet()