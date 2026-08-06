nums = [1,2,1]
rest = [-1]*len(nums)
nums = nums + nums
print(nums)
stk = []
mapping = {}
for num in range(len(nums)):
    while stk and nums[num] > nums[stk[-1]]:
        popped = stk.pop()
        mapping[popped] = nums[num]
    stk.append(num)
for x in range(len(rest)):
    if x in mapping:
        rest[x] = mapping[x]
print(rest)
