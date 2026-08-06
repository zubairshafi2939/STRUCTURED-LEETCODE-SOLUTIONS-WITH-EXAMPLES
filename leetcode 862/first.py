from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        subArr = deque()
        total = 0
        rest = 9999999999
        data = 9999999999
        for x in nums:
            subArr.append(x)
            total += x
            while total > k:
                print("True")
                rest = min(rest,len(subArr))
                toAdd = subArr.popleft()
                total -= toAdd
            while subArr and subArr[0] < 1:
                total -= subArr.popleft()
            if total == k:
                rest = min(rest,len(subArr))
        if rest == data:
            return -1
        return rest
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
nums = [54,-5,53,-19,85]
k = 119
sol = Solution()
print(sol.shortestSubarray(nums,k))