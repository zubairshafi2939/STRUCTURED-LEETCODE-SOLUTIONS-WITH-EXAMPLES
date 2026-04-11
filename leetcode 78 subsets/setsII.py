nums = [4,4,4,1,4]
result = []
chk = set(result)
nums.sort()
for x in nums:
    output = []
    output.append(x)
    dummy = list(result)
    for i in range(len(dummy)):  # i am using shallow copy 
        temp = dummy[i] + [x] # this is the way. firstly i am using dummy[i].append(x) [ye kaam karen to result me b changing atti hai jo me dummy me karungaa]
        
        if temp not in result:
            result.append(temp)
    if output not in result:
        result.append(output)
result.append([])
print(result)