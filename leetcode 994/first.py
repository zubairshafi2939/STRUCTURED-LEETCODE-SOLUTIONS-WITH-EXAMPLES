class Solution(object):
    def orangesRotting(self, grid):
        def isRotten(x,y,grid,toCheck):
            if x > 0:
                if grid[x-1][y] == toCheck:
                    return True
            if x < len(grid)-1:
                if grid[x+1][y] == toCheck:
                    return True
            if y > 0:
                if grid[x][y-1] == toCheck:
                    return True
            if y < len(grid[0])-1:
                if grid[x][y+1] == toCheck:
                    return True
            return False
        def Possible(x,y,grid,FirstCheck):
            if FirstCheck == False:
                return True
            first = second = third = fourth = 1
            if x == 0:
                first = 0
            elif grid[x-1][y] == 0:
                first = 0
            if y == 0:
                second = 0
            elif grid[x][y-1] == 0:
                second = 0
            if x == (len(grid)-1):
                third = 0
            elif grid[x+1][y] == 0:
                third = 0
            if y == len(grid[0]):
                fourth = 0
            elif grid[x][y+1] == 0:
                fourth = 0
            if first == 0 and second == 0 and third == 0 and fourth == 0:
                return False
            else:
                return True
    


        condition = True
        toCheck = 2
        result = 0
        FirstCheck = True
        while condition:
            condition = False
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == 1 and isRotten(x,y,grid,toCheck):
                        if not Possible(x,y,grid,FirstCheck):
                            return -1
                        grid[x][y] = toCheck + 2
                        condition = True
            if condition:
                result += 1
            toCheck += 2
            FirstCheck = False
        return result
            
                    


        