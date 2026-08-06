
class Solution(object):
    def reverseStr(self, s, k):
        groups = [s[i:i+k] for i in range(0, len(s), k)]
        # return groups
        for x in range(0,len(groups),k):
            groups[x] = groups[x][::-1]
        return "".join(groups)

        """
        :type s: str
        :type k: int
        :rtype: str
        """
sol = Solution()
print(sol.reverseStr("abcdefg",8))