class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        max_val = max(nums)
        if total%2 == 1 or max_val > (total//2):
            return False
        
        required = total//2
        nums.sort()
        dp = [False]*(required+1)
        value = 0
        for x in nums:
            for y in range(len(dp)-1,-1,-1):
                if dp[y] == True and y+x < len(dp):
                    # print("True for ", x, " and ", )
                    dp[y+x] = True
            value += x
            if value < len(dp):
                dp[value] = True
            dp[x] = True
        return dp[-1]

        """
        :type nums: List[int]
        :rtype: bool
        """

nums = [1,5,11,5]
sol = Solution()
print(sol.canPartition(nums))