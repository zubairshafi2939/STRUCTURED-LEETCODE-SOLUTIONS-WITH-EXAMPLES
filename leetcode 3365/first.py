class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        data = {}
        for i in range(0,len(s),k):
            data[s[i:i+k]] = data.get(s[i:i+k],0)+1
        for i in range(0,len(t),k):
            if t[i:i+k] not in data:
                return False
            else:
                t[i:i+k] -= 1
        return max(data.values()) == 0 and min(data.values) == 0
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """

s = "abcd"
t = "cdab"
k = 2    

sol = Solution()
print(sol.isPossibleToRearrange(s,t,k))