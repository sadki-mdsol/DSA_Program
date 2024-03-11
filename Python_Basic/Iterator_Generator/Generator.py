def toptensquare():
    n = 1
    while n <=10:
        sq = n * n
        yield sq
        n +=1

v1 = toptensquare()

for i in v1:
    print(i)


# def yield_ftn():
#     yield 10

# print(yield_ftn().__next__())
# print("HEllo")
