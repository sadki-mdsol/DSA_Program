class Student:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = Student(m1,m2)
        return s3

    def __sub__(self,other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2

        s3 = Student(m1,m2)
        return s3
    
    def __gt__(self,other):
        if (self.m1+self.m2)  > (other.m1+other.m2):
            return True
        else:
            return False

s1 = Student(50,160)
s2 = Student(60,90)

s3 = s1+s2
print (s3.m1)
print (s3.m2)

s3 = s2-s1
print (s3.m1)
print (s3.m2)

if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")


