class Parent:
    def phone(self):
        print("Nokia Phoen")

class Child(Parent): #here child is overridding the phone() of parent
    def phone(self):
        print("Child Phone")

c1 = Child()
c1.phone()