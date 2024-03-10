class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no =roll_no
        self.lap = self.Laptop()

    def show(self):
        print(self.roll_no,self.name)

    def display_all_details(self):
        self.show()
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.cpu = 'i5'
            self.ram = 18
            self.brand = 'Mac'

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Sneha',20)
s2 = Student('Vijay',18)

s1.show()
s2.show()

#call the inner class method show via s1 object

print("call the inner class method show via s1 object--------")
s1.lap.show()
s2.lap.show()

# call inner class method in the outer class method

print("call inner class method in the outer class method--------")
s1.display_all_details()
s2.display_all_details()


#creating the inner Class Object outside the outer class
print("creating the inner Class Object outside the outer class--------")
outer_lap = Student.Laptop()
outer_lap.show()