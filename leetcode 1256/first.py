class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums)%k != 0:
            return False
        data = {}
        num = sorted(set(nums))
        for x in nums:
            data[x] = data.get(x,0)+1
        i = 0
        while i < len(num):
            if data[num[i]] <= 0:
                i += 1
            else:
                data[num[i]] -= 1
                for y in range(i+1,i+k):
                    if y >= len(num) or num[y-1] != (num[y]-1):
                        return False
                    data[num[y]] -= 1
                    if data[num[y]] < 0:
                        return False

        return True
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        

nums = [1,2,2,3,3,4]
k = 3
sol = Solution()
print(sol.isPossibleDivide(nums,k))