class A:
    def Feature1(self):
        print("From Feature 1")
    
    def Feature2(self):
        print("From Feature 2")


class B:
    def Feature3(self):
        print("From Feature 3")

class C(A,B):
    def Feature4(self):
        print("From Feature 4")


c1 = C()
c1.Feature4()
c1.Feature1()
c1.Feature2()
c1.Feature3()

