class Solution(object):
    def subarraySum(self, nums, k):
        dp = [False]*(k+1)
        dp[0] = True
        rest = 0
        for x in nums:
            for y in range(len(dp)-1,-1,-1):
                if dp[y-x]:
                    dp[y] = True
                    if y == (len(dp)-1):
                        rest += 1
        return rest
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

nums = [-1,-1,1]
k = 1
sol = Solution()
print(sol.subarraySum(nums,k))