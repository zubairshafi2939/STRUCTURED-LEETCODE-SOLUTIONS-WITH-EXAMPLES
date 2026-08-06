class Solution(object):
    def arrangeWords(self, text):
        data = text.split(" ")
        max_len = 0
        for x in data:
            max_len = max(max_len,len(x))
        bucket = [[] for x in range(max_len+1)]
        for x in data:
            bucket[len(x)].append(x)
        rest = []
        for x in bucket:
            if x:
                for y in x:
                    rest.append(y.casefold())
        text = " ".join(rest)
        change = text[0].capitalize()
        return change + text[1:]
        """
        :type text: str
        :rtype: str
        """
        
text = "Keep calm and code on"
sol = Solution()
print(sol.arrangeWords(text))