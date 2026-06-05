nums1 = [1,2,3]
nums2 = [2,3,4]
set1 = set(nums1)
set2 = set(nums2)
rest = []
for x in nums1:
    if x in set2:
        rest.append(x)
        break
for x in nums2:
    if x in set1 and x < rest[0]:
        rest[0] = x
if len(rest) == 0:
    print(-1)
else:
    print(rest[0])
        
