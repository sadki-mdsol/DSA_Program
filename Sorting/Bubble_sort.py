def sort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j] > arr[j+1]:
                swap = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = swap
            
    print(arr)


# sort([3,2,8,5,6])


def sort_negative_for(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                swap = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = swap
    print(arr)

sort_negative_for([6,5,7,3,9,2])
    
