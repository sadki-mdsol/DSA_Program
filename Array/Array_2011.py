# 2011. Final Value of Variable After Performing Operations

# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

def operationArray(arr):
    x = 0
    for a in arr:
        if a in ('++X','X++'):
            x=x+1
        elif a in ('--X','X--'):
            x= x-1
    return x



if __name__ == '__main__':
    arr = ["--X","X++","X++","--X","--X"]
    print(operationArray(arr))