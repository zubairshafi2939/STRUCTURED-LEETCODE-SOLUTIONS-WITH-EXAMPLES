nums1 = [1,2,4]
nums2 = [1,2,3,4]
stk = []
data = {}
for num in nums2:
    while stk and num > stk[-1]:
        popped = stk.pop()
        data[popped] = num
    stk.append(num)
rest = []
for num in nums1:
    if num not in data:
        rest.append(-1)
    else:
        rest.append(data[num])
print(rest)
