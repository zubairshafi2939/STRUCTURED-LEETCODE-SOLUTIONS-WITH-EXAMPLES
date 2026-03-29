nums = [2,3,4,6,8]
temp = list(nums)
temp.sort()
rest = {}
for x in range(len(temp)):
    if temp[x] not in rest:
        rest[temp[x]] = x
result = []
for x in range(len(nums)):
    result.append(rest[nums[x]])
return result
# time complexity O(NlogN)