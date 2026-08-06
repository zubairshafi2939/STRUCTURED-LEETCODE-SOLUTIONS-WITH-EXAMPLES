class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for x in nums:
            num = abs(x)
            if nums[num-1] < 1:
                result.append(num)
                continue
            nums[num-1] *= -1
        return result
            

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
sol = Solution()
print(sol.findDuplicates( [1,1,2]))