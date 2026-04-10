# understanded and done easily but. give a try after some days
amount = 4
coins = [1,2,3]
dp = [amount +1] * (amount + 1)
dp[0] = 0
sp = [amount + 1] * (amount + 1)
sp[0] = 0
for x in range(1, amount +1):
    c = 0
    for coin in coins:
        if x-coin >= 0:
            c+= 1
            dp[x] = min(dp[x],1 + dp[x - coin])
    sp[x] = c
print( dp[-1] if dp[-1] != amount +1 else -1)
print(sp)