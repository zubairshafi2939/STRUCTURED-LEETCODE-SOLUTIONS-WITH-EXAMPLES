class Solution(object):
    def firstUniqueEven(self, nums):
        data = {}
        for x in nums:
            data[x] = data.get(x,0)+1
        for x in nums:
            if x %2 == 0 and data.get(x,0) >= 2:
                return x
            
        """
        :type nums: List[int]
        :rtype: int
        """
sol = Solution()
print(sol.firstUniqueEven([3,4,2,5,4,6]))