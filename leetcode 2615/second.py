class Solution(object):
    def distance(self, nums):
        data = {}
        result = []
        for x in range(len(nums)):
            if nums[x] not in data:
                data[nums[x]] = [x,1]
            else:
                data[nums[x]][0] += x
                data[nums[x]][1] += 1 
        for x in range(len(nums)):
            add = x*data[nums[x]][1]
            add -= data[nums[x]][0]
            result.append(add)
        return result
    
        """
        :type nums: List[int]
        :rtype: List[int]
        """

sol = Solution()
print(sol.distance([1,3,1,1,2]))