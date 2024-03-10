class Person:
    def __init__(self) -> None:
        self.name='Sneha'
        self.age=30

    def update(self):
        self.age = 28

    def print_person(self):
        print("name: {}, age:{}".format(self.name,self.age))

p1 = Person()
p2 = Person()

p1.name='Vijay'
p1.update()

p1.print_person()
p2.print_person()
