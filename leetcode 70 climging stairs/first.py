n = 0
dp = [1] * (n+1)
for x in range(1,n+1):
    if x-1 >=0 and x-2 >=0:
        dp[x] = dp[x-1] + dp[x-2]
print(dp[-1])