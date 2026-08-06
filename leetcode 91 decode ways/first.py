class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0":
            ways = 0
        else:
            ways = 1
        for x in range(1,len(s)):
            digit = int(s[x-1]+s[x])
            if digit > 9 and digit < 27:
                ways += 1
        return ways

        """
        :type s: str
        :rtype: int
        """
        
sol = Solution()
print(sol.numDecodings("1111"))