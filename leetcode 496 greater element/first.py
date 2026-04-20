nums1 = [2,4]
nums2 = [1,2,3,4]
rest = []
for x in nums1:
    result = -1
    for y in range(len(nums2)-1,-1,-1):
        if nums2[y] == x:
            rest.append(result)
            break
        if nums2[y] > x:
            result = nums2[y]
print(rest)
