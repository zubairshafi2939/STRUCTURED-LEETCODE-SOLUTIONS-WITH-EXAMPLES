class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        matrix = obstacleGrid
        n = len(matrix[0])
        m = len(matrix)
        for x in range(n):
            if matrix[0][x] == 1:
                for i in range(x,n):
                    matrix[0][i] = 0
                break
            else:
                matrix[0][x] = 1
        for x in range(1,m):
            if matrix[x][0] == 1:
                for i in range(x,m):
                    matrix[i][0] = 0
                break
            else:
                matrix[x][0] = 1
        for x in range(1,m):
            for y in range(1,n):
                if matrix[x][y] == 1:
                    matrix[x][y] = 0
                else:
                    matrix[x][y] = matrix[x-1][y]+matrix[x][y-1]
        return matrix

        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

sol = Solution()
print(sol.uniquePathsWithObstacles([[0],[1]]))