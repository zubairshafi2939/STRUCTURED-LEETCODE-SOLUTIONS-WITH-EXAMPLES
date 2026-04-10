amount = 4
coins = [1,2,3]
dp = [0] * (amount + 1)
dp[0] = 1
print(dp)

for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] += dp[i - coin]

print(dp[amount])