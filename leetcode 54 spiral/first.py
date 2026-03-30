matrix = [[1],
          [4],
          [7]]
x = []
while matrix and bool(matrix[0]):
    x += matrix.pop(0)
    if len(matrix) >= 2:
        last = len(matrix[1])-1
        for i in range(len(matrix)-1):
            x.append(matrix[i].pop(last))
    print(matrix)
    if len(matrix) >0:
        while matrix[len(matrix)-1]:
            x.append(matrix[len(matrix)-1].pop())
        matrix.pop(len(matrix)-1)

    if matrix and bool(matrix[0]):
        for y in matrix:
            x.append(y.pop(0))
    print(x)



# print(matrix)
print(x)
    


