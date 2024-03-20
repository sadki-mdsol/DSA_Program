def intersection(nums1, nums2):
    size = len(nums2) if len(nums2)<len(nums1) else len(nums1)
    final_arr = set()
    if len(nums2)<len(nums1):
        for i in range(0,len(nums2)):
            if nums2[i] in nums1:
                final_arr.add(nums2[i])
    else:
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                final_arr.add(nums1[i])


    return list(final_arr)

nums1=[1,2,2,1]
nums2=[2,2]
print(intersection(nums1,nums2))


