nums = [8,1,2,2,3]
temp = list(nums)
temp.sort()
# print(temp)
rest = {}
for x in range(len(temp)):
    if temp[x] not in rest:
        rest[temp[x]] = x
# print(rest)
result = []
# for x in range(len(nums)):
#     result.append(rest[nums[x]])
# print(result)
print(rest[nums[0]])
print(nums)



