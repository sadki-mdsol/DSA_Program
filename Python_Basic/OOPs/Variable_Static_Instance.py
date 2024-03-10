#if we update the static variable via class name then it will reflect in all objects
#but if we update via object then it will change to this object not the class Varibale

class Car:
    wheels = 4
    def __init__(self) -> None:
        self.com='BMW'
        self.mil =10

    def displayCar(self):
        print(self.com,self.mil,Car.wheels,self.wheels)


c1 = Car()
c2 = Car()

# print(id(c1.wheels))
# print(id(c2.wheels))

print("C1 car detaisl")
c1.displayCar()
Car.wheels = 11

# print(id(c1.wheels))
# print(id(c2.wheels))
print("C2 car detaisl")
c2.displayCar()

print("C1 car detaisl")
c1.displayCar()
print("C2 car detaisl")
c2.displayCar()