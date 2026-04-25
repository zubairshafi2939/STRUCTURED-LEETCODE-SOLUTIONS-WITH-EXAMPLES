nums = [1,2,3,4,5,6,7,8,9,10]
nm = {}
for x in nums:
    nm[x] = 0
mex = 1
for x in range(len(nums)):
    if nm[nums[x]] == 1:
        continue
    else:
        pst = nums[x]
        ngt = pst
        seq = 1
        while (pst+1) in nm:
            seq += 1
            nm[pst] = 1
            pst += 1
        while (ngt-1) in nm:
            seq += 1
            nm[ngt] = 1
            ngt -= 1
        mex = max(mex,seq)
print(mex)
        
