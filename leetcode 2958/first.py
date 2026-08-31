class Solution(object):
    def maxSubarrayLength(self, nums, k):
        l = 0
        r = 0
        data = {}
        rest = 0
        while r < len(nums):
            if (data.get(nums[r],0)+1) >k:
                data[nums[l]] = data.get(nums[l],0)-1
                l += 1
                continue
            data[nums[r]] = data.get(nums[r],0)+1
            rest = max(rest,r-l+1)
            r += 1
        return rest

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
nums = [1,2,1,2,1,2,1,2]
k = 1
sol = Solution()
print(sol.maxSubarrayLength(nums,k))

