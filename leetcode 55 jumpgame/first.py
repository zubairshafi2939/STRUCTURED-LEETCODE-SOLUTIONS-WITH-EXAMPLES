nums = [2,3,1,0,4]
length = len(nums)-(3+2)

index = len(nums)-1
while index >=0:
    if nums[index] == 0:
        target = index
        while nums[index-1] == 0:
            index -= 1
        index -= 1
        conditioner = False
        while index >=0:
            if (nums[index] + index) > target:
                conditioner = True
                index -= 1
            elif nums[index] == 0:
                index += 1
                continue
            else:
                index -= 1
        if conditioner == False:
            # return False
            pass
    else:
        index -= 1

    





