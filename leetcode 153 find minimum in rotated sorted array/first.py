nums = [3,4,5,1,2]
l = 0
h = len(nums)-1
while(l<=h):
    mid = int((l+h)/2)
    if l == h:
        print("found at", l)
        break
    if nums[mid] <= nums[h]:
        h = mid -1
    else:
        l = mid+1
print("nothing")