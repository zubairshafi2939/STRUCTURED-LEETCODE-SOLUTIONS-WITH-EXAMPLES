n = 1
# arr = [[1,2,3,4],[12,5],[11,6],[10,9,8,7]]
arr = []
top = 0
bottom = n-1
left = 0
right = n-1
no = 1
for x in range(n):
    array = []
    for y in range(n):
        array.append(no)
        no +=1
    arr.append(array)
print(arr)
no = 1
while n>0:
    if n == 1:
        arr[top][left] = no
        break
    for x in range(left,n+left):
        arr[top][x] = no
        no += 1
    top += 1
    for x in range(top,bottom):
        arr[x][right] = no
        no += 1
    lr = right
    right -= 1
    for x in range(lr,left-1,-1):
        arr[bottom][x] = no
        no += 1
    for x in range(bottom-1,top-1,-1):
        arr[x][left] = no
        no += 1
    bottom -=1
    left += 1
    n = n-2
print(arr)

