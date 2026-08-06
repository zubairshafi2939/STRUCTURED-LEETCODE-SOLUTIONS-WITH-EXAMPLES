nums1 = [4,1,2]
nums2 = [1,3,4,2]
stk = []
mapping = {}
for num in nums2:
    while stk and num > stk[-1]:
        ptr = stk.pop()
        mapping[ptr] = num
    stk.append(num)
for x in range(len(nums1)):
    if nums1[x] in mapping:
        nums1[x] = mapping[nums1[x]]
    else:
        nums1[x] = -1
print(nums1)