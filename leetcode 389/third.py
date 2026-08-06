# #suggested by ai. doing on my own
# class Solution(object):
#     def findTheDifference(self, s, t):
        

#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """

# sol = Solution()
# print(sol.findTheDifference("a","aa"))
# # t = "something"
# # s = list(t)
# # s.sort()
# # print(s)
s = "abcde"
t = "abcdef"
res = 0
for x in s:
    res ^= ord(x)
for x in t:
    res ^= ord(x)
print(chr(res))
