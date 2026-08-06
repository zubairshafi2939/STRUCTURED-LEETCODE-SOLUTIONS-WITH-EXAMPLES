class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        index = 0
        for x in range(1,k+1):
            if nums[index]<0:
                nums[index] *= -1
                if index+1 < len(nums) and nums[index+1] <=0:
                    index += 1
            elif nums[index] == 0:
                break
            else:
                number = k-x
                if number%2 == 1:
                    nums[index] *= -1
                    break
        return sum(nums)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
sol = Solution()
print(sol.largestSumAfterKNegations([2,-3,-1,5,-4],2))