print("Enter number 1")
number1 = int(input())

print("Enter number 2")
number2 = int(input())
print("Number 1 ",number1)
print("Number 2 ",number2)

# #via 3rd variable
# temp = number1
# number1 = number2
# number2 = temp

# print("Number 1 ",number1)
# print("Number 2 ",number2)

# without 3rd variable
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print("Number 1 ",number1)
print("Number 2 ",number2)
