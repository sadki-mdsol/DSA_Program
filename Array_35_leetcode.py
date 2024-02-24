# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Solution 1 : Nomral way

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


# Solution 2 : Bianry search
def binarySearch(nums,target):
    print(nums,target)
    
    # l = 0
    # r = len(nums)-1
    # N = len(nums)-1
    le,ri = 0,len(nums)-1

    while le <= ri:
        mid = (le+ri)//2
        val = nums[mid]

        if target < nums[mid]:
            ri = mid-1
        elif target > nums[mid]:
            le= mid+1
        else :
            return mid
    return le


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    print(searchInsert(nums,target))
    print(binarySearch(nums,target))
