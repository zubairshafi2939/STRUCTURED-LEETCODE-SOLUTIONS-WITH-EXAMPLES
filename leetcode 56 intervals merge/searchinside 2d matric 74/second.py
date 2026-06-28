matrix = [[1]]
l = 0
h = len(matrix)-1
target = 5
variable = -1
while (l <=h):
    mid = (l+h)//2
    if target <= matrix[mid][-1] and target >= matrix[mid][0]:
        variable = mid
        break
    elif target > matrix[mid][-1]:
        l = mid + 1
    elif target < matrix[mid][0]:
        h = mid - 1
if variable == -1:
    return False
else:
    return True
l = 0
h = len(matrix[0])
mid = matrix[mid]
while(l<=h):
    m = (l+h)//2
    if mid[m] == target:
        print("found the data")
        print("index is: ", m)
        break
    elif mid[m] > target:
        h = m - 1
    else:
        l = m + 1