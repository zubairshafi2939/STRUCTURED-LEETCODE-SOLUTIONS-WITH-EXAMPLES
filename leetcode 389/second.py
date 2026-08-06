class Solution(object):
    def findTheDifference(self, s, t):
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for x in t:
            if d[x] <= 0:
                return x
            else:
                d[x] -= 1

        """
        :type s: str
        :type t: str
        :rtype: str
        """

sol = Solution()
print(sol.findTheDifference("a","aa"))
# t = "something"
# s = list(t)
# s.sort()
# print(s)