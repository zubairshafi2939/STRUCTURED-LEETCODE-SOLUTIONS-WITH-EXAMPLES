nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
i = -1
index = m+n -1
m= m -1
n = n-1
while n > -1 or m > -1:
    while n > -1 and m > -1:
        if nums1[m] > nums2[n]:
            nums1[index] = nums1[m]
            m -= 1
        else:
            nums1[index] = nums2[n]
            n -= 1
        index -= 1
    while m > -1:
        nums1[index] = nums1[m]
        m -= 1
        index -= 1
    while n > -1:
        nums1[index] = nums2[n]
        index -= 1
        n -= 1
print(nums1)