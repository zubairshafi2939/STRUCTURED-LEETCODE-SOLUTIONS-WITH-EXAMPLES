from collections import deque
class Solution(object):
    def rearrangeArray(self, nums):
        positives = deque()
        negatives = deque()
        i = 0
        while i < len(nums):
            if nums[i]>=0:
                positives.append(nums[i])
            else:
                negatives.append(nums[i])
            i+= 1
        rest = []
        while positives and negatives:
            rest.append(positives.popleft())
            rest.append(negatives.popleft())
        return rest
        """
        :type nums: List[int]
        :rtype: List[int]
        """

sol = Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))