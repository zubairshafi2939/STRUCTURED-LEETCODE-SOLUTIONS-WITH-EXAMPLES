nums = [1,2,4,2,6,1,4,0,3,8]
jump = 0
maxlen = nums[0]
i = 1
while i < len(nums):
    temp = maxlen
    while i < len(nums) and i <= maxlen:
        temp = max(temp, i + nums[i])
        i += 1
    maxlen = temp
    jump += 1
    print("just")
print(jump)