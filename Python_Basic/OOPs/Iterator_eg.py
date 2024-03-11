class IncrementBy5:
    def __init__(self) -> None:
        self.num =1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 100:
            val = self.num
            self.num += 5
            return val
        else:
            raise StopIteration
        

t10 = IncrementBy5()

for i in t10:
    print(i)