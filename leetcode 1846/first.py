arr =[2, 2, 5, 2, 2]
arr.sort()
required = 1
arr[0] = required
for x in range(1,len(arr)):
    if arr[x] > required:
        required += 1
        arr[x] = required
print(arr)