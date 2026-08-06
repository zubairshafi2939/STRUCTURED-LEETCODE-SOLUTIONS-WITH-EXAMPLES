class Solution(object):
    def numOfStrings(self, patterns, word):
        data = set(word)
        total = 0
        for x in patterns:
            if x in word:
                total += 1
            
        return total

        
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
sol = Solution()
print(sol.numOfStrings(["a","abc","bc","d"],"abc"))