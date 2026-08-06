grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","1","0"],
  ["0","0","0","1","1"]
]
def backtrack(grid,x,y):
    if grid[x][y] != "1":
        return
    grid[x][y] = "-1"
    if (x+1) < len(grid):
        backtrack(grid,x+1,y)
    if (x-1) >= 0:
        backtrack(grid,x-1,y)
    if (y+1) < len(grid[0]):
        backtrack(grid,x,y+1)
    if (y-1) >= 0:
        backtrack(grid,x,y-1)
    return
count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "1":
            backtrack(grid,x,y)
            count += 1
print(count)