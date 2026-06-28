matrix = [[1,1,1],[1,0,1],[1,1,1]]
rest = []
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if matrix[x][y] == 0:
            rest.append([x,y])
print("result is: ", rest)
for x in rest:
    start = 0
    while start < len(matrix):
        matrix[start][x[1]] = 0
        start += 1
    left = 0
    while left < len(matrix[0]):
        matrix[x[0]][left] = 0
        left += 1
print(matrix)