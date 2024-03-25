nums = [6,5,5]
max_count = 0
value = 0
mapper = {}
for i in nums:
    if i in mapper:
        mapper[i] +=mapper[i]
    else:
        mapper[i] = 1
    if mapper[i] > max_count:
        max_count = mapper[i]
        value = i

print(value)
