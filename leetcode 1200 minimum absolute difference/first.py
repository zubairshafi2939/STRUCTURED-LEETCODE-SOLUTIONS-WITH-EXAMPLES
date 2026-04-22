arr = [1,-1]
arr.sort()
less = float('inf')
rest = []
for x in range(len(arr)-1):
    value = arr[x+1] - arr[x]
    if value < less:
        print("True")
        less = value
        rest = []
        rest.append([arr[x],arr[x+1]])
    elif value == less:
        rest.append([arr[x],arr[x+1]])
print(rest)
