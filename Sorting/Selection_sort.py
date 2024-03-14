def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i,len(arr)):
            if arr[j]<arr[min]:
                min=j
        # only one swap
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
        print(arr)

    print("Final Output------")
    print(arr)

selection_sort([5,3,8,6,7,2])