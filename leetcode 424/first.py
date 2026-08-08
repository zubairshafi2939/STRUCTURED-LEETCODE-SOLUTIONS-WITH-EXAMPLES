class Solution(object):
    def characterReplacement(self, s, k):
        if len(s) == 1:
            return 1
        data = {s[0]:1}
        left = 0
        right = 1
        result = 0
        while right< len(s):
            data[s[right]] = data.get(s[right],0)+1
            length = right - left + 1
            if length > (max(data.values())+k):
                result = max(result,length-1)
                data[s[left]] = data.get(s[left],0)-1
                left += 1
                right += 1
                continue
            result = max(result,length)
            right += 1
        return result
        """
        :type s: str
        :type k: int
        :rtype: int
        """
# happy to see that i just reached to that solution at on my own. Without a single thing to get from claude or any ai. Just took me an hour. But i guess its worth it
s = "A"
k = 0
sol = Solution()
print(sol.characterReplacement(s,k))
