nums = [2,-1,1,1]
rest = nums[0]
result = rest
neg = [nums[0],nums[0]]
negrest =  rest
flag = True
for x in range(1, len(nums)):
    if rest <= 0:
        rest = nums[x]
        result = max(result, rest)
    else:
        rest = rest * nums[x]
        result = max(result, rest)
    if neg[0] == 0:
        neg[0] = nums[x]
        neg[1] = nums[x]
        flag = True
    elif neg[0] < 0 and flag == True:
        neg[1] = nums[x]
        neg[0] = neg[0] * nums[x]
        flag = False
        nasty = max(neg[0],neg[1])
        negrest = max(nasty ,negrest)
        # print(negrest)
        # print("one time only")
        continue
    else:

        neg[0] = neg[0] * nums[x]
        neg[1] = neg[1] * nums[x]
    # print(neg[0])
    nasty = max(neg[0],neg[1])
    negrest = max(nasty ,negrest)
    
print(result)
print(negrest)

    
  