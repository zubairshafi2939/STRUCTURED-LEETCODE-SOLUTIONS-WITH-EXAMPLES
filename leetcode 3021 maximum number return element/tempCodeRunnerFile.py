nums = [2,2,4,4,16,16,256]
nums.sort()
print(nums)
result = 0
for x in range(1,len(nums)):
    if nums[x-1] == nums[x]:
        score = 2
        i = x+1
        ptr = nums[x]*nums[x]
        data = set()
        while i < len(nums):
            if ptr == nums[i]:
                result = max((score+1),result)
                if nums[i] == nums[i-1] and nums[i] not in data:
                    score += 2
                    data.add(nums[i])
            if ptr < nums[i]:
                ptr *= ptr
            i += 1
print(result)



