grid = [[2,3],[2,5]]
for x in range(1, len(grid)):
    grid[x][0] += grid[x-1][0]
for x in range(1, len(grid[0])):
    grid[0][x] += grid[0][x-1]

for x in range(1,len(grid)):
    for y in range(1,len(grid[0])):
        grid[x][y] += min(grid[x-1][y],grid[x][y-1])
