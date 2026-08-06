class Solution(object):
    def lastRemaining(self, n):
        data = [x for x in range(1,n+1)]
        while True:
            prev = []
            if len(data) == 1:
                break
            for x in range(1,len(data),2):
                prev.append(data[x])
            data = prev
            prev = []
            if len(data) == 1:
                break
            for y in range(len(data)-2,-1,-2):
                prev.insert(0,data[y])
            data = prev
        return data[-1]
        """
        :type n: int
        :rtype: int
        """
sol = Solution()
print(sol.lastRemaining(2))