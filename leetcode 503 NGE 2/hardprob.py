nums = [3,3]
for x in range(len(nums)):
    index = x
    ctr = 0
    real = nums[x]
    while index < len(nums):
        if nums[x] < nums[index]:
            ctr += 1
        if ctr >= 2:
            nums[x] = nums[index]
            break
        index += 1
    if real == nums[x]:
        nums[x] = -1
print(nums)
