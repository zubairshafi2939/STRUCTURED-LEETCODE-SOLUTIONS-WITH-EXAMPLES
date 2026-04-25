nums = [1,3,1,1,2]
data = {}
result = [0] * (len(nums))
for x in range(len(nums)):
    if nums[x] not in data:
        data[nums[x]] = [x]
    else:
        for j in data[nums[x]]:
            result[x] = result[x] + abs(x - j)
        data[nums[x]].append(x)
        mylist = data[nums[x]]
        for num in mylist:
            result[num] += abs(num-x)
        
print(result)
# for x in range(len(nums)):
#     mylist = data[nums[x]]
#     i = x
#     rest = 0
#     for j in mylist:
#         rest = rest + abs(i-j)
#     result.append(rest)
# print(result)
    
