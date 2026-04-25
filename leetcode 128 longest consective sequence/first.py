nums = [1,2,2,3,3,4]
nums.sort()
seq = 1
mex = 1
print(nums)
for x in range(1,len(nums)):
    if (nums[x] - nums[x-1]) == 1:
        print(True)
        seq += 1
    elif (nums[x] - nums[x-1]) >1:
        mex = max(mex,seq)
        seq = 1
mex = max(seq, mex)
print(mex)