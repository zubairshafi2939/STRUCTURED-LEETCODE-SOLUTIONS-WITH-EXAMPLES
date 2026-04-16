nums1 = [1,2,3,0,0,0]
m = 3
temp = nums1[0:3]
nums2 = [2,5,6]
n = 3
i = 0
x = 0
index = 0
while i < m or x < n:
    while i < m and x < n:
        if temp[i] < nums2[x]:
            nums1[index] = temp[i]
            i += 1
        else:
            nums1[index] = nums2[x]
            x+= 1
        index += 1
    while i < m:
        nums1[index] = temp[i]
        i += 1
        index += 1
    while x < n:
        nums1[index] = nums2[x]
        x += 1
        index +=1
print(nums1)
