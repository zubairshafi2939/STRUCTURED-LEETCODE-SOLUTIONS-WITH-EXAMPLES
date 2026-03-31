arr = [48,62,39]
rest = 0
for x in range(1,len(arr)-1):
    if  arr[x-1] < arr[x] > arr[x+1]:
        l = r = x
        
        while l >0 and arr[l] > arr[l-1]:
            l -= 1
        while r <= len(arr)-2  and arr[r+1] < arr[r]:
            r+=1
        print(l , "and right is : ", r)
        rest = max(rest, r-l+1)
print(rest)

