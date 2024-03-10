
# w.r.t Single inhertiance

# if we have init in both the init's & create a object of child class then it will invoke only clid class constructor
class A:
    def __init__(self) -> None:
        print("A's init")


class B(A):
    def __init__(self) -> None:
        print("B's init")


b1  = B()

#if we have init in the parent class only then it will invoke parent class init

class D:
    def __init__(self) -> None:
        print("D's init")

class E(D):
    pass

d1 = D()

# if we want to call the super class init in the sub class of init then use the super()

class F:
    def __init__(self) -> None:
        print("From E's init")

class G(F):
    def __init__(self) -> None:
        super().__init__()
        print("From G's init")

g1 =G()