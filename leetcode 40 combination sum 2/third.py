class Solution(object):
    def combinationSum2(self, candidates, target):
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
# sol = Solution()
# print(sol.combinationSum2([1,1,1,1,1,1,1,2,2],8))
candidates = [10,1,2,7,6,1,5]
candidates.sort()
print(candidates)
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]