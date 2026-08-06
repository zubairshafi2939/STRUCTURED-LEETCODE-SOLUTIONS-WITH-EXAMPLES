class Solution(object):
    def majorityElement(self, nums):
        length = len(nums)//3
        data = {}
        for x in nums:
            data[x] = data.get(x,0) + 1
        result = []
        for x,y in data.items():
            if y > length:
                result.append(x)
        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
sol = Solution()
print(sol.majorityElement([3,2]))