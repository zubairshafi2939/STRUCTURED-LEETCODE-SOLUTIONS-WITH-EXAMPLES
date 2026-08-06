class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        matrix = obstacleGrid
        print(obstacleGrid)
        n = len(matrix[0])
        m = len(matrix)
        if matrix[0][0] == 1:
            return 0
        matrix[0][0] = 1
        for x in range(1,n):
            if matrix[0][x] == 1:
                matrix[0][x] = 0
            else:
                matrix[0][x] = matrix[0][x-1]
        for x in range(1,m):
            if matrix[x][0] == 1:
                matrix[x][0] = 0
            else:
                matrix[x][0] = matrix[x-1][0]
        for x in range(1,m):
            for y in range(1,n):
                if matrix[x][y] == 1:
                    matrix[x][y] = 0
                else:
                    matrix[x][y] = matrix[x-1][y] + matrix[x][y-1]



        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))