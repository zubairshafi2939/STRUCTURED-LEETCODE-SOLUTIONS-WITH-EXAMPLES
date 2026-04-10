n =  127
dp = [0] * (n+1)
num = 1
for x in range(1,n+1):
    if num<<1 <= x:
        num = num<<1
    dp[x] = dp[x-num] + 1
print(dp[-1])

