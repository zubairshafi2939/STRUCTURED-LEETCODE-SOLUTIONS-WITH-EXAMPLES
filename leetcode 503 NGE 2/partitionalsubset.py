nums = [1,5,11,5]
nums.sort()
l = 0
r = len(nums)-1
left_sum = nums[l]
lstk = [nums[l]]
rstk = [nums[r]]
right_sum = nums[r]
while l < r:
    if (l+1) == r and left_sum == right_sum:
        print("True")
    if left_sum > right_sum:
        r -= 1
        right_sum += nums[r]
        rstk.append(nums[r])
    else:
        l += 1
        left_sum += nums[l]
        lstk.append(nums[l])
    