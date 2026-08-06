class Solution(object):
    def lastRemaining(self, n):
        l = 1
        r = n
        prev = 1
        while l < r:
            if n%2 == 0:
                l += prev
            else:
                l += prev
                r -= prev
            prev *= 2
            n = n//2
            if l == r:
                return l
            if n%2 == 0:
                r = r - prev
            else:
                r -= prev
                l += prev
            prev *= 2
            n = n //2
        return l
            
        """
        :type n: int
        :rtype: int
        """
sol = Solution()
print(sol.lastRemaining(4))