class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
s = "3002"
i = 0
indexes = []
index = 0
while i < len(s):
    if s[i] == '0':
        s = s[:i] + s[i+1:]
        indexes.append(index)
        index += 1
        continue
    i += 1
    index += 1
print(s)
print(indexes)
