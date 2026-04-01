class Solution(object):
    def lengthOfLastWord(self, s):
        ret = 0
        prev = []
        for x in s:
            if x == " ":
                prev.append(ret)
                ret = 0
            else:
                ret+=1
        prev.append(ret)
        while prev[len(prev)-1] == 0:
            prev.pop()
        return prev[len(prev)-1]
        """
        :type s: str
        :rtype: int
        """
        