triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
for x in range(len(triangle)):
    for y in range(len(triangle[x])):
        if x >= 1:
            if y == 0:
                triangle[x][y] = triangle[x][y] + triangle[x-1][y]
            elif y == len(triangle[x])-1:
                triangle[x][y] = triangle[x][y] + triangle[x-1][y-1]
            else:
                value = triangle[x][y]
                triangle[x][y] = min(value + triangle[x-1][y],value+triangle[x-1][y-1])
print(triangle[-1])