class Solution(object):
    def findTheDifference(self, s, t):
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for x in range(len(s)):
            if s[x] != t[x]:
                return t[x]
        return t[-1]

        """
        :type s: str
        :type t: str
        :rtype: str
        """

sol = Solution()
print(sol.findTheDifference("a","a"))
# t = "something"
# s = list(t)
# s.sort()
# print(s)