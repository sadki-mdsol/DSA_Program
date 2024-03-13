def search_ele(arr,s_ele):
    l = 0
    u = len(s)-1

    while l<=u:
        mid = (l+u)//2
        if arr[mid]==s_ele:
            return ("Element Found at {} for {}".format(mid,arr))
            
            # return Found
        elif arr[mid] > s_ele:
            u = mid-1
            # mid = (u + l)/2
            # search_ele(arr,s_ele,l,u,m)
        elif arr[mid] < s_ele:
            l = mid+1
            # mid = (u + l)/2
            # search_ele(arr,s_ele,l,u,m)

    return "Not Found"



s = [30,50,60,70,80,90,100]
s_ele = 30
# l = 0
# u = len(s)
# mid = (l+u)/2
print(search_ele(s,s_ele))

