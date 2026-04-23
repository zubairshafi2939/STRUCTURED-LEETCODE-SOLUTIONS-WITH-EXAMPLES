nums = [1,2,3,4,5,6,7]
k = 3
if len(nums) <=1:
    print(nums)
k = k % len(nums)
stk = []
for x in range(k):
    a = nums.pop()
    stk.append(a)
for x in range(k):
    a = stk.pop(0)
    nums.insert(0,a)
print(nums)
