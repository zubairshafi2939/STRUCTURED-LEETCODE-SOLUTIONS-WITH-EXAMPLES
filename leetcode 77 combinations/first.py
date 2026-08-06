n = 5
k = 3
minus = k-1
res = [0]*k
index = 0
result = []
def backtrack(start, end, index,res):
    res[index] = start 
    if index == k-1:
        result.append(list(res))
        return
    end += 1
    for x in range(start+1,end+1):
        backtrack(x,end,index+1,res)
for i in range(1,n-minus+1):
    backtrack(i,n-minus,index,res)
print(result)
