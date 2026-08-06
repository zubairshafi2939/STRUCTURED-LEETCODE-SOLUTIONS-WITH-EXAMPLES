nums = [2,4,0,9,6]
stk = []
mapping = {}
first = [-1]*len(nums)
for num in nums:
    while stk and num > stk[-1]:
        popped = stk.pop()
        mapping[popped] = num
    stk.append(num)
for i in range(len(first)):
    if nums[i] in mapping:
        first[i]  = mapping[nums[i]]
    else:
        first[i] = nums[i] * -1
print(first)
print(nums)
rest = [-1]*len(nums)
stk = []
mapping_2 = {}
for i in range(len(nums)):
    while stk and first[i]>nums[stk[-1]]:
        if first[stk[-1]] == first[i]:
            break
        popped = stk.pop()
        mapping_2[popped] = first[i]
    stk.append(i)
print(mapping_2)