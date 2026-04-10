nums = [1,2,3]
result = []
for x in nums:
    output = []
    output.append(x)
    dummy = list(result)
    for i in range(len(dummy)):
        temp = dummy[i] + [x]
        result.append(temp)
    result.append(output)
print(result)