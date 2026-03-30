matrix = [[1,2,3],[4,5,6],[7,8,9]]
x = []
while matrix and bool(matrix[0]):
    x += matrix.pop(0)
    if len(matrix) >= 2:
        last = len(matrix[1])-1
        for i in range(len(matrix)-1):
            x.append(matrix[i].pop(last))
    if len(matrix) > 0:
        while matrix[len(matrix)-1]:
            x.append(matrix[len(matrix)-1].pop())
        matrix.pop(len(matrix)-1)

    if matrix and bool(matrix[0]):
        for l in range(len(matrix)-1,-1,-1):
            x.append(matrix[l].pop(0))
# return x
print(x)