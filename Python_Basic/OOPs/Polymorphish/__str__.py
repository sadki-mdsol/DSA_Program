class int:
    def __init__(self,m1) -> None:
        self.m1 = m1

    def __str__(self) -> str:
        return "XYZ"
    
a = int(10)
print(a)

class Student:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __str__(self) -> str:
        # return "XYZ"
        return '{} {}'.format(self.m1,self.m2)
    
s1 = Student(69,59)
print(s1)

