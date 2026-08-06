class Solution(object):
    def subarraySum(self, nums, k):
        counter = {0:1}
        for n in nums:
            for total,count in counter.items():
                counter[total+n] = counter.get(total+n,0)+count
        return counter
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

sol = Solution()
print(sol.subarraySum([1,1,1],2))