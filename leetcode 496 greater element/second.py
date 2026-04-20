nums1 = [4,1,2]
nums2 = [1,3,4,2]
rest = []
data = {}
for x in range(len(nums2)):
    data[nums2[x]] = x
for x in range(len(nums1)):
    result = -1
    for y in range(data[nums1[x]],len(nums2)):
        if nums2[y] > nums1[x]:
            result = nums2[y]
            break
    rest.append(result)
print(rest)
print(data)