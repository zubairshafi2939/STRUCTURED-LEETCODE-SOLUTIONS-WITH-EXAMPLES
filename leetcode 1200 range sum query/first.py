# [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
nums = [-2,0,3,-5,2,-1]
data = [0] * (len(nums))
data[0] = nums[0]
for x in range(1,len(nums)):
    data[x] = data[x-1] + nums[x]
print(data)

if 0-1< 0:
    print(data[2])
else:
    print(data[0] - data[2])