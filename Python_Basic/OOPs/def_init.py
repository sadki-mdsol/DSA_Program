class Computer:
    def __init__(self,cpu,ram) -> None:
        print("Initialisation of {}".format(self))
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self,self.cpu,self.ram)


c1 = Computer('MacPro',19)
c2 = Computer('Dell',20)

c1.config()
c2.config()

