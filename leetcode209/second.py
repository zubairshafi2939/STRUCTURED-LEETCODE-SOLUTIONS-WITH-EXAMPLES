target = 4
nums = [1,4,4]
left = 0
right = 1
value = nums[left] + nums[right]
ret = 99999999
while right < len(nums):
    if value >= target:
        ret = min(ret,right-left+1)
        print("right:", right , "left:",left)
        value = value - nums[left]
        left += 1
    else:
        right += 1
        if right <len(nums):
            value = value + nums[right]
print(ret)



