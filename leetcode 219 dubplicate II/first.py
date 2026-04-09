nums = [1,0,1,1] #solved in first attempt but heres better approach i guess you should go for it 
k = 1
ret = {}
for x in range(len(nums)):
    if nums[x] not in ret:
        ret[nums[x]] = x
    else:
        if abs(ret[nums[x]]-x) <=k:
            print(True) 
print(False)
print(ret)