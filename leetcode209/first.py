target = 7 
nums = [2,3,1,2,4,3]
left = 0
right = 1
while left < len(nums):
    value = nums[left] + nums[right]
    if value >= target:
        print(right - left+1)
        if right-left == 1:
            break
        left += 1
    else:
        if right < len(nums)-1:
            right+=1
    if left >= len(nums) -1:
        break
    print("something is cooking")
    
