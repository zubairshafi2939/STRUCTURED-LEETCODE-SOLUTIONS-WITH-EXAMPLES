candidates = [2,3,5]
result = []
target = 8
def back(cand,target,res,i = 0, total = 0, ):
    res.append(cand[i])
    total += cand[i]
    if total == target:
        copy = list(res)
        result.append(copy)
        res.pop()
        return
    if total > target:
        res.pop()
        return 
    for n in range(i,len(cand)):
        back(cand,target,res,n,total)
    res.pop()
for x in range(len(candidates)):
    back(candidates,target,[],x,0)
print(result)
    