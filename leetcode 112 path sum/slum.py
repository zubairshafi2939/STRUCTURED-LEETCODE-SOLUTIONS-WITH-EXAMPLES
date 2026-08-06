class Solution(object):
    def maxDigitRange(self, nums):
        result = []
        for x in nums:
            arr = [int(y) for y in str(x)]
            arr.sort()
            result.append(arr[-1]-arr[0])
        real = 0
        if len(result) == 1:
            return result[-1]
        n = -1
        i = result[n]
        while i == result[-1]:
            real += i
            n -= 1
            i = result[n]
        print(real)
        return real
            
            
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
sol = Solution()
print(sol.maxDigitRange([5724,111,350]))