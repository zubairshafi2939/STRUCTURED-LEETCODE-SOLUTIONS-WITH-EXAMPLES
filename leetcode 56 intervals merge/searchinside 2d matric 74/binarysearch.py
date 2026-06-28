nums = [2,5,6,8,9]
l = 0
h = len(nums)-1
target = 7
while(l<=h):
    mid = (l+h)//2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        l = mid + 1
    else:
        h = mid - 1
print(mid)