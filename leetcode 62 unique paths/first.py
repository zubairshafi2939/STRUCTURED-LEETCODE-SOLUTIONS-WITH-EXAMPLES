class Solution(object):
    def uniquePaths(self, m, n):
        matrix = [[1]*n]*m
        for x in range(1,m):
            for y in range(1,n):
                matrix[x][y] = matrix[x-1][y]+matrix[x][y-1]
        return matrix[-1][-1]
        """
        :type m: int
        :type n: int
        :rtype: int
        """


sol = Solution()
print(sol.uniquePaths(3,7))