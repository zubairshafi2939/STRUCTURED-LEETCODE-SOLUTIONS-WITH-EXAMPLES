# understanded and done easily but. give a try after some days
amount = 4
coins = [1,2,3]
#creating array of same lenght + 1 and stored a number (can also -1 as numbers are positive)
dp = [amount +1] * (amount + 1) 
#now storing in at 0 index 0 because to how many coins are required to make zero = 0
dp[0] = 0
for x in range(1, amount +1):
    for coin in coins:
        if x-coin >= 0: # if coins value is equal to x that means dp[0] which is zero and we added + 1 so 1 coin is needed.
            # and if value is less than coin than we can check how many coins are required to create the other number which we already know
            dp[x] = min(dp[x],1 + dp[x - coin])
print( dp[-1] if dp[-1] != amount +1 else -1)
