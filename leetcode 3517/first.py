class Solution(object):
    def smallestPalindrome(self, s):
        alphabets = [0]*26
        rest = ""
        for x in range(len(s)//2):
            alphabets[ord(s[x])-97]+= 1
        for y in range(len(alphabets)):
            for i in range(alphabets[y]):
                rest += chr(y+97)
        return rest + rest[::-1] if len(s)%2 == 0 else rest + s[len(s)//2] + rest[::-1]

        return alphabets
            
        """
        :type s: str
        :rtype: str
        """

sol = Solution()
print(sol.smallestPalindrome("babab"))