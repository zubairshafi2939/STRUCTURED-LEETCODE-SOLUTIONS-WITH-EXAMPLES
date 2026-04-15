nums = [1,1,2]
nums.sort()
data = set()
d = nums[len(nums)-1] + 99
n = 0
for x in range(len(nums)):
    if nums[x] in data:
        nums[x] = d
        n += 1
    else:
        data.add(nums[x])
nums.sort()
t = len(nums) - 1
for x in range(n):
    nums[t] = "_"
    t -= 1


print(data)
print(nums)
print(n)

