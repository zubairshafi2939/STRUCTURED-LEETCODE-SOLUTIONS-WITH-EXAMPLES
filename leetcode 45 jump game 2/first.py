nums = [1,2,4,2,6,1,4,0,3,8]
dp = [99999] * len(nums)
dp[0] = 0
for x in range(1, len(nums)):
    for y in range(0, x):
        length = y + nums[y]
        if length >= x:
            dp[x] = min(dp[x],dp[y]+1)
print(dp)