class Solution(object):
    def wordBreak(self, s, wordDict):
        s = s + "t"
        dp = [" "]  + [9]*(len(s))
        for x in range(len(s)):
            for word in wordDict:
                start = x-len(word)
                if start>=0 and dp[start] != 9 and s[start:x]==word:
                    for i in dp[start]:
                        if dp[x] == 9:
                            dp[x] = []
                        dp[x].append([i[0]+" "+s[start:x]])
        data = dp[-2]
        result = []
        for x in range(len(data)):
            result.append(data[x][0].lstrip())
        return result

        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
sol = Solution()
print(sol.wordBreak(s,wordDict))
# ["cats and dog","cat sand dog"]