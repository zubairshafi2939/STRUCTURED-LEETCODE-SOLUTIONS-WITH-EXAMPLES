class Solution(object):
    def scoreDifference(self, nums):
        player = [0,0]
        index = 0
        for x in range(len(nums)):
            if nums[x]%2 == 1:
                index = 1 if index == 0 else 0
            if (x+1)%6 == 0:
                index = 1 if index == 0 else 0
            player[index] += nums[x]
        return player[0] - player[1]
        """
        :type nums: List[int]
        :rtype: int
        """
nums = [2,4,2,1,2,1]
sol = Solution()
print(sol.scoreDifference(nums))

