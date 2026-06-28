nums = [-1,1,0,-3,3]
left = [nums[0]]
right = [nums[-1]]
low = len(nums)-2
for x in range(1,len(nums)):
    left.append(left[x-1]*nums[x])
    right.insert(0,right[0]*nums[low])
    low -= 1
rest = []
for x in range(len(nums)):
    if x == 0:
        rest.append(right[1])
    elif x == (len(nums)-1):
        rest.append(left[len(nums)-2])
    else:
        rest.append(left[x-1]*right[x+1])
print(rest)
