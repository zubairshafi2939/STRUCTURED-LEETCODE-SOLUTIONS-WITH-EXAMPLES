nums = [1,5,11,5]
nums.sort()
l = 0
r = 0
for x in range(len(nums)):
    if l > r:
        r += nums[x]
    else:
        l += nums[x]
print(l,r)
