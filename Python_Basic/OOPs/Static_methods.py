# if we want to work with some other type of variabel not witrh static or insatnce variabel
#use decorator @staticmethod & no arguments


class Person:
    def __init__(self):
        self.name= 'XYZ'

    @staticmethod
    def soemthing():
         print("External code")

Person.soemthing()