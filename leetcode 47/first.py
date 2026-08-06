nums = [1,2,3]
rest = [-11]*len(nums)
start = 0
end = len(nums)
data_set = set()
result = []
def back(rest,index,startIndex,end):
    if startIndex in data_set:
        return
    data_set.add(startIndex)
    rest[index] = nums[startIndex]
    if index >= (end-1):
        if rest in result:
            data_set.remove(startIndex)
            return
        result.append(list(rest))
        data_set.remove(startIndex)
        return
    for x in range(0,end):
        back(rest,index+1,x,end)
    data_set.remove(startIndex)
    return
for i in range(len(nums)):
    back(rest,0,i,end)
print(result)
        

