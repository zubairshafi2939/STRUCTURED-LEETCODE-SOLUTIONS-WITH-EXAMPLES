class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0 or n < 0:
            return False
        n = abs(n)
        if n > 3:
            t = 3
            while t < n:
                t*= 3
            if t == n:
                return True
        else:
            t = 3
            while t > n:
                t = t /3
            if n == t:
                return True
        return False

sol = Solution()
print(sol.isPowerOfThree(19684))