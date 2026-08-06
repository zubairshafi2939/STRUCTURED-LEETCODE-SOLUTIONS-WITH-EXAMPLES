class Solution(object):
    def wordPattern(self, pattern, s):
        word = s.split(" ")
        data  = {}
        used = set()
        for x in range(len(pattern)):
            if pattern[x] not in data:
                if word[x] in used:
                    return False
                used.add(word[x])
                data[pattern[x]] = word[x]
            elif word[x] != data[pattern[x]]:
                return False
        return True
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
sol = Solution()
print(sol.wordPattern( "abba", "dog cat cat dog"))