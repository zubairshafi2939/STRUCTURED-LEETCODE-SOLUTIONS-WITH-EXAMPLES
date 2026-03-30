matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
x = []

x = matrix.pop(0)   
if len(matrix) >= 2:
    last = len(matrix[1])-1
    for i in range(len(matrix)-1):
        x.append(matrix[i].pop(last))
print("value of matrix is", matrix)
while matrix and bool(matrix[0]):
    x.append(matrix[len(matrix)-1].pop())
    print("one time")
matrix.pop(len(matrix)-1)

if matrix:
    for y in matrix:
        x.append(y.pop(0))



print(matrix)
print(x)
    


