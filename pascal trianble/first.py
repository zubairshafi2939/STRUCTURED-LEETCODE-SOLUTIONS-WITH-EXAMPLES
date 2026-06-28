numRows = 3
result = []
for x in range(1,numRows):
    inner = []
    index = x - 2
    print("here")
    for y in range(x):
        if index >= 0 and y > 0 and y < x:
            print("inner for ", y)
            math = result[index][y] + result[index][y-1]
            inner.append(math)
        else:
            inner.append(1)
    result.append(inner)
    print(result)

        
