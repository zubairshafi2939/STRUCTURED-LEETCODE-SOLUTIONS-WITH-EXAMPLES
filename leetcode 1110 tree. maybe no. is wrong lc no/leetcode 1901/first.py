class Solution(object):
    def findMiddleIndex(self, nums):
        left = [0]* len(nums)
        right = [0]* len(nums)
        sum = 0
        for x in range(len(nums)):
            sum += nums[x]
            left[x] = sum
        sum = 0
        for x in range(len(nums)-1,-1,-1):
            sum += nums[x]
            right[x] = sum
        for x in range(1,len(nums)-1):
            if left[x-1] == right[x+1]:
                return x
        if len(nums)>=2:
            if left[1] == 0:
                return 0
            if right[-2] == 0:
                return len(right)-1
        
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """

sol = Solution()
print(sol.findMiddleIndex([2,3,-1,8,4]))
