#so the final solution is here. i just fixed the bug. the key issue is
# he used r<= len(arr) -1 and l >=0 while he had to use < > just rather 
# with = sign
arr = [2,3,4,5,6,4,3,5]
ret = 0

for i in range(1, len(arr)-1):

    if arr[i-1] < arr[i] > arr[i+1]:
        l=r=i

        while l>0 and arr[l]> arr[l-1]:
            l-=1

        while r<len(arr)-1 and arr[r] > arr[r+1]:
            r+=1
        ret =max(ret, r-l+1)

print(ret)