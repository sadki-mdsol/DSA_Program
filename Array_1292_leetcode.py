# 1929. Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.




def concatArray(nums):
    #shallow Copy
    ans = nums.copy()

    for n in nums:
        ans.append(n)
    return ans

if __name__ == '__main__':
    nums = [1,3,5,6]
    print(concatArray(nums))