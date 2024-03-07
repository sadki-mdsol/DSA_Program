number = int(input("Enter the number"))

for i in range(2,number):
    if number%i==0:
        print("Not Prime")
        break
else:
    print("Prime")