nums = [2,2,2,3,3,4,5,5,5]
count = 0
prev = -1
index = 0
for x in range(len(nums)):
    if nums[x] == prev:
        count += 1
        if count >=3:
            continue
    else:
        count = 1
        prev = nums[x]
    nums[index] = nums[x]
    index += 1
print(nums)