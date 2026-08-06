from collections import heapq
class Solution(object):
    def maxScore(self, nums):
        heap = []
        total = 0
        score = 0
        for x in nums:
            if x < 1:
                heapq.heappush(heap,x)
            else:
                total += x
                score += 1
        for y in heap:
            if score <= 0:
                return score
            score += heap
        return score

        """
        :type nums: List[int]
        :rtype: int
        """

nums = [2,-1,0,1,-3,3,-3]
sol = Solution()
print(sol.maxScore(nums))