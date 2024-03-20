def missingNumber(nums):
    for i in range(1,len(nums)+1):
        if i not in nums:
            return i
    return 0

print(missingNumber([3,0,1]))
        