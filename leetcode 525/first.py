nums = [0,1,0,1,0,1,1,1,0,0,0]
prefix = [nums[0]] * len(nums)
for x in range(1,len(nums)):
    prefix[x] = prefix[x-1] + nums[x]
print(prefix)
