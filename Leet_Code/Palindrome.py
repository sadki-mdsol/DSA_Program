def isPalindrome( x):
    original_x = str(x)
    str_x= ''
    print(original_x)
    for i in range(len(str(x))-1,-1,-1):
        str_x = str_x + str(original_x[i])

    if original_x == str_x:
        return True
    return False

print(isPalindrome(121))