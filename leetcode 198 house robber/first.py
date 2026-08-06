class Solution(object):
    def rob( nums):
        for x in range(1,len(nums)):
            if x < 2:
                nums[x] = max(nums[x],nums[x-1])
                continue
            nums[x] = max(nums[x]+nums[x-2],nums[x-1])
        return nums[-1]

        """
        :type nums: List[int]
        :rtype: int
        """


# sol = Solution()
# print(sol.rob([1,2,3,1]))
# print(sol.rob([2,1,1,2]))
# print(sol.rob([1,6,1,2]))

index = 1
index = int(not index)
print(index)