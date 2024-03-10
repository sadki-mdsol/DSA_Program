#instance method work with instance object
#self is required for the instance method

# 2 type
# Accessor (getter)
#mutators (setter)

class Car:
    def __init__(self) -> None:
        self.com='BMW'
        self.mil =10

    def displayCar(self): #accessor
        print(self.com,self.mil)

    def updateCar(self): #mutator
        self.mil = 20


c1 = Car()
c2 = Car()

c1.displayCar()
c1.updateCar()
c1.displayCar()
c2.displayCar()