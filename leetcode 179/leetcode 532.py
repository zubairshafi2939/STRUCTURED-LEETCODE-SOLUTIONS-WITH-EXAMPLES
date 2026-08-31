class Solution(object):
    def findPairs(self, nums, k):
        data = set(nums)
        result = 0
        for x in data:
            if (x-k) in data:
                result += 1
        return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
nums = [1,2,3,4,5]
k = 1
sol = Solution()
print(sol.findPairs(nums,k))