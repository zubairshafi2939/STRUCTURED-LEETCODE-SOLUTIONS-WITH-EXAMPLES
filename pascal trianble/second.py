numRows = 5
result = []
for x in range(1,numRows+1):
    inn = [1] * x
    iterations = x - 2
    if iterations > 0:
        for y in range(1,x-1):
            inn[y] = result[iterations][y] + result[iterations][y-1]
    result.append(inn)
print(result)


