

# 1470. Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].


def shuffleArray(nums,n):
    left = 0
    mid = right = n
    
    ans = []
    while left != mid:
        ans.append(nums[left])
        ans.append(nums[right])

        left = left+1
        right=right+1
    return ans

    
if __name__ == '__main__':
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    print(shuffleArray(nums,n))