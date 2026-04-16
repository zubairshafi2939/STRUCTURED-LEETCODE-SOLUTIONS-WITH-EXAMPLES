nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
i = -1
x = -1
index = n+m-1
n = n -1
m = m -1
while m > i or n > x:
    while m > i and x < n:
        if nums1[m] < nums2[n]:
            nums1[index] = nums1[m]
            m -= 1
        else:
            nums1[index] = nums2[n]
            n-= 1
        index -= 1
    while m > i:
        nums1[index] = nums1[m]
        m -= 1
        index -= 1
    while n > x:
        nums1[index] = nums2[n]
        n -= 1
        index -=1
print(nums1)
