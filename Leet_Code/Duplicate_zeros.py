arr = [1,0,2,3,0,4,5,0]
def solution1(arr):
    i=0
    while i < len(arr):
        if arr[i] == 0:
            j= len(arr)-1
            while j > i:
                arr[j] = arr[j-1]
                j-=1
            i=j+1
        i+=1


def solution2(arr):
    i=0
    j = len(arr)-1
    while i < len(arr):
        if arr[i] == 0 and i < j:
            j-=1
        i+=1
    print(arr,i,j)

    i = len(arr)-1
    while j >= 0:
        arr[i] = arr[j]
        if arr[j] == 0:
            i = i-1
            arr[i]=0
        print(arr)
            
        j-=1
        i-=1

    print(arr)


arr = [8,4,5,0,0,0,0,7]
solution2(arr)