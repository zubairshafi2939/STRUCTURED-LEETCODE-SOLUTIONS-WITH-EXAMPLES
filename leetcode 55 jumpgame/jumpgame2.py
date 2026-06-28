nums = [1,5,2,2,2,2,5]
#dynamic programming method
dp = [0] * len(nums)
stack = [[nums[0],0]]
# minimum use horaa ho, or uski range me ho
enteringIndex = -2
for x in range(1, len(nums)):
    temp = x - stack[-1][-1]
    while temp > nums[stack[-1][-1]]:
        stack.pop(-1)
        enteringIndex = -1
    dp[x] = 1 + stack[-1][0]
    stack.insert(0,[dp[x],x])
print(dp)

    
