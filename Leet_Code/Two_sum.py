def twoSum(array,target):
    arr = {}
    for i in range(len(array)):
        if target-array[i] in arr:
            return [arr[target-array[i]],i]
        arr[array[i]] = i
            
    return []

array = [3,3]
target = 6
print(twoSum(array,target))