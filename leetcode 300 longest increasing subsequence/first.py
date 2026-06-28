nums = [10,9,2,5,3,7,101,18]
dp = [1] * len(nums)
print(dp)
for x in range(len(nums)):
    for y in range(x-1,-1,-1):
        if nums[y] < nums[x]:
            dp[x] = max(dp[x], dp[y]+1)
print(max(dp))