nums = [3,30,44,5,9]
nums.sort()
greatest = len(str(nums[-1]))
data = {}
for x in range(len(nums)):
    data[nums[x]] = x
print(data)