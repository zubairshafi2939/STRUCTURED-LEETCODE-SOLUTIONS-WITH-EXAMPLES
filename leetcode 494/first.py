class Solution(object):
    def findTargetSumWays(self, nums, target):
        counter = {0:1}
        for n in nums:
            temp = {}
            for total,count in counter.items():
                temp[total+n] = temp.get(total+n,0)+count
                temp[total-n] = temp.get(total-n,0)+count
            counter = temp
        return counter.get(target,0)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

nums = [100, 200, 300]
target = 400
sol = Solution()
print(sol.findTargetSumWays(nums,target))