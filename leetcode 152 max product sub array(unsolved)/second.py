nums = [-2,0,-1]
left = 0
right = 0
rest = 0
result = 0
while right < len(nums):
    if left == right :
        if nums[left] <= 0:
            result = max(result, nums[left])
            left += 1
            right += 1
        else:
            rest = nums[left]
            right += 1
    elif nums[right] <=0:
        result = max(result, rest)
        left = right
    else:
        rest = rest * nums[right]
        right += 1
print(result)
