class Solution(object):
    def rearrangeArray(self, nums):
        next_positive = 0
        next_negative = 1
        result = [0]*len(nums)
        for x in nums:
            if x >=0:
                result[next_positive] = x
                next_positive += 2
            else:
                result[next_negative] = x
                next_negative += 2
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """

sol = Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))