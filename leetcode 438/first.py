class Solution(object):
    def findAnagrams(self, s, p):
        data = {}
        for x in p:
            if x not in data:
                data[x] = 1
            else:
                data[x]+=1
        lenght  = len(p)
        for i in range(lenght):
            if s[i] in data:
                data[s[i]] -= 1
        result = []
        for y in range(len(s)-lenght):
            max_value = max(data.values())
            if max_value == 0:
                result.append(y)
            if s[y] in data:
                data[s[y]] += 1
            if s[y+lenght] in data:
                data[s[y+lenght]] -= 1
        return result
            
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

sol = Solution()
print(sol.findAnagrams("cbaebabacd","abc"))       