def move_zeros(nums):
    j=0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j+=1
    while j < len(nums):
        nums[j]=0
        j+=1
    return nums

print(move_zeros([1,0,3]))
print(move_zeros([1,0]))
print(move_zeros([0]))
print(move_zeros([0,1,0,3,12]))
print(move_zeros([4,2,4,0,0,3,0,5,1,0]))
