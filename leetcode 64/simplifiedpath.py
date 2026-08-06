class Solution(object):
    def simplifyPath(self, path):
        arr = []
        i = 0
        while i < len(path):
            start = i
            while i < len(path) and path[i] != "/":
                i+= 1
            arr.append(path[start:i])
            i+= 1
        stk = []
        for x in range(len(arr)):
            if arr[x] == "." or arr[x] == "":
                continue
            if arr[x] == "..":
                stk.pop()
                continue
            stk.append(arr[x])
        result = ""
        for x in stk:
            result += "/" + x
        return result

        """
        :type path: str
        :rtype: str
        """
sol = Solution()
print(sol.simplifyPath("/a/./b/../../c/"))
