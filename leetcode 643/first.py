class Solution(object):
    def findMaxAverage(self, nums, k):
        total = 0
        for x in range(k):
            total += nums[x]
        start = 0
        max_avg = total / k
        for y in range(k, len(nums)):
            total = total + nums[y] - nums[start]
            start += 1
            max_avg = max(max_avg, total/k)
        
        return max_avg

        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))