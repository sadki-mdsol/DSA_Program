class TopTen:
    def __init__(self) -> None:
        self.num =1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
t10 =TopTen()

for t in t10:
    # print("Iterator is {}".format(next(t10)))
    print(t)