nums = []
nums = [10,44,75,100,55,80]
print(nums)

print(nums[0])
print(nums[-1])
print(nums[0:])
print(nums[:])
print(nums[:10]) #will not throw error


nums[0] = 20
print(nums)

num_diff = [80,'Sneha',7.5]
print(num_diff)

array_in_array=[num_diff,nums]
print(array_in_array)


#build in fucnitons

nums.append(404)
print(nums)

nums.insert(5,404) #404 will insert at index 5
print(nums)

nums.pop()
print(nums)

nums.pop(3) #here opo with index will remoev that index value
print(nums)

nums.extend([1,2,3,70])
print(nums)
(a1,*b1,c1) = nums

print(a1,b1,c1)
print(min(nums))
print(max(nums))
print(sum(nums))