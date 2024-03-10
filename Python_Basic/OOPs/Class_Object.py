class Computer:

    def config(self):
        print("i5,16GB,15T")


c1 = Computer()
c1.config()

Computer.config(c1)