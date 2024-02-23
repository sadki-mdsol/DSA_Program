# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


def searchInsert(nums,target):
    for key,value in enumerate(nums):
        if value == target:
            return key
        elif value > target :
            return key
        elif key+1 >= len(nums):
            return key+1
        elif value < target and nums[key+1]>target:
            return key+1
    

if __name__ == '__main__':
    nums = [1]
    target = 0
    print(searchInsert(nums,target))