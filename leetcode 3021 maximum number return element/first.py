nums = [5,4,1,2,2,16]
nums.sort()
might = set()
for x in range(1,len(nums)):
    if nums[x-1] == nums[x]:
        might.add(nums[x])
maxval = max(nums)
total = []
for x in might:
    print(x)
    reserve = [x]
    ptr = x
    while ptr < maxval:
        ptr = ptr * ptr
        if ptr in nums:
            reserve.append(ptr)
    total.append(reserve)
print(total)