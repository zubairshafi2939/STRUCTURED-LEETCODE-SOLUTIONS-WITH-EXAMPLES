candidates = [3,1,3,5,1,1]
target = 8
result = []
def back(cand,target,res,i = 0, total = 0, ):
    res.append(cand[i])
    total += cand[i]
    if total == target:
        copy = list(res)
        copy.sort()
        if copy in result:
            return
        result.append(copy)
        res.pop()
        return
    if total > target:
        res.pop()
        return 
    for n in range(i+1,len(cand)):
        back(cand,target,res,n,total)
    res.pop()
for x in range(len(candidates)):
    back(candidates,target,[],x,0)
print(result)
    