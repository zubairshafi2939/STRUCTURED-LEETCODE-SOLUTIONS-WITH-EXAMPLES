#solved but with exceptions are handled very badly i guess
# just optimize  it and then rewrite the code
class Solution(object):
    def minSubArrayLen(self, target, nums):
        if len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0
        for x in nums:
            if x >= target:
                return 1
        left = 0
        right = 1
        value = nums[left] + nums[right]
        ret = 99999999
        while right < len(nums):
            if value >= target:
                ret = min(ret,right-left+1)
                value = value - nums[left]
                left += 1
            else:
                right += 1
                if right <len(nums):
                    value = value + nums[right]
        if ret == 99999999:
            return 0
        else:
            return ret
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        