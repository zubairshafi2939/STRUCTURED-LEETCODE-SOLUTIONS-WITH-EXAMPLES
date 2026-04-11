nums = [2,5,3,3]
k = 2
left = 0
right = k
rest = []
print(max(nums[left:right]))
while right <= len(nums):
    rest.append(max(nums[left:right]))
    right += 1
    left +=1
print(rest)
