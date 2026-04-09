# couldn't get the solution and then after watching video my first attempt
arr = [2,1,4,7,3,2,5]
rest = 0
for x in range(1,len(arr)-1):
    if  arr[x-1] < arr[x] > arr[x+1]:
        # l = 0
        # r = 0
        # forget what i had to do now watching
        l = r = x
        while l >=0 and arr[l] > arr[l-1]:
            l -= 1
        while r <= len(arr)-1 and arr[r] > arr[r+1]:#basicaly there is an issue in the solvers code so i had to fix it on my own first on this line too. 
            r+=1
        
        rest = max(rest, r-l+1)
print(rest)

