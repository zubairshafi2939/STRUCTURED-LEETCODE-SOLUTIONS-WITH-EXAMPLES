class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for x in range(1, amount +1):
            for coin in coins:
                if x-coin >= 0:
                    dp[x] += dp[x-coin]
        return dp
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
sol = Solution()
print(sol.coinChange([1,2,5],5))