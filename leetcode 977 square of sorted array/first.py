nums = [-4,-1,0,3,10]
result = []
pst = len(nums)
ngt = -1
for x in range(len(nums)):
    ngt = x
    if nums[x] >=0:
        pst = x
        ngt = x-1
        break
while pst < len(nums) or ngt >= 0:
    if pst<len(nums) and ngt >= 0:
        if nums[pst] < abs(nums[ngt]):
            result.append(nums[pst]*nums[pst])
            pst += 1
        else:
            result.append(nums[ngt]*nums[ngt])
            ngt -=1
    elif pst >=len(nums) and ngt >=0:
        result.append(nums[ngt]*nums[ngt])
        ngt -=1
    else:
        result.append(nums[pst]*nums[pst])
        pst += 1
print(result)


