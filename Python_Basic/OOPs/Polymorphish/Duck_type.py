# many class no relation ship 
# Mandatory it should have common method name
# we can call the method by passign a object

class pycharm:
    def execute(self):
        print("Compiling")
        print("Execute")


class VSCode:
    def execute(self):
        print("Compiling")
        print("Execute")
        print("Spell Check")
        print("Git check")


class Laptop:
    def code(self,ide):
        ide.execute()


py = pycharm()
vs =VSCode()
l1 = Laptop()

print("Pycharm---------")
l1.code(py)
print("VS code---------")
l1.code(vs)
print("Pycharm---------")
l1.code(pycharm())
