#if we want to work with the static variables use static methods


class Student:
    school='DR'

    def __init__(self) -> None:
        self.name = 'Sneha'
        self.age = '20'

    #for static we need to used decorator @classmethod & ftn arg by default it should be cls
    @classmethod
    def class_info(cls):
        print("School Info")
        print(cls.school)
        cls.school = 'DRM'
        cls.address ='Solapur'
        print(cls.school,cls.address)

Student.class_info()