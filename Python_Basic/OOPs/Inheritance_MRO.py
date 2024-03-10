#method Resolution Order

# in multiple inhertiance thw super () will invoke either method or init based on the extends order from left to right


class A:
    def __init__(self) -> None:
        print("A's init")


class B:
    def __init__(self) -> None:
        print("B's init")


class C(B,A):
    def __init__(self) -> None:
        super().__init__()
        print("C's init")


c1 = C()
