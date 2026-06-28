nums = [4,4,16,16,256,256,65536,65536]
nums.sort()
result = 1
smain = set()
for x in range(1,len(nums)):
    if nums[x-1] == nums[x]:
        ptr = nums[x]* nums[x]
        score = 2
        i = x+1
        main = set()
        once = True
        while i < (len(nums)):
            if nums[i] == ptr:
                print("value of nums:", nums[i], nums[x])
                result = max(result, score + 1)
                if nums[i] in main and once == True:
                    score += 2
                    print("Statement true and score is ", score)
                    once = False
                main.add(nums[i])
            elif nums[i] > ptr:
                ptr = ptr*ptr
                if ptr == nums[i]:
                    print("maybe true")
                    main.add(nums[i])
                    result = max(result,score+1)
            i += 1
        
print(result)
