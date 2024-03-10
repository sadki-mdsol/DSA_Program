class A:
    def Feature1(self):
        print("From Feature 1")
    
    def Feature2(self):
        print("From Feature 2")


class B(A):
    def Feature3(self):
        print("From Feature 3")


b1 = B()
b1.Feature1()
b1.Feature2()
b1.Feature3()