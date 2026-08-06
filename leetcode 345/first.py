class Solution(object):
    def reverseVowels(self, s):
        l = 0
        r = len(s)-1
        data = set(['a','e','i','o','u'])
        while l < r:
            while l < len(s) and s[l] not in data:
                l += 1
            while r >=0 and s[r] not in data:
                r -= 1
            if l >= r:
                break
            else:
                s = s[:l]+s[r]+s[l+1:r]+ s[l] + s[r+1:]
            r -= 1
            l += 1
        return s
        """
        :type s: str
        :rtype: str
        """
        
sol = Solution()
print(sol.reverseVowels("Icecreamae"))
