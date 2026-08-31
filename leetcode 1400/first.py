class Solution(object):
    def canConstruct(self, s, k):
        data = {}
        for x in s:
            data[x] = data.get(x,0)+1
        rest = []
        for x,y in data.items():
            rest.append(y)
        rest.sort()
        for x in range(len(rest)):
            if x >= k and rest[x] == 1:
                return False
            if x >= k:
                return True
        return True
                

        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
s = "annabelle"
k = 2
sol = Solution()
print(sol.canConstruct(s,k))