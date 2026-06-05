n = 4
k = 2
data = []
for x in range(k):
    data.append(x+1)
# print(data)

def backtrack(l,p):
    while l[-1] <= p:
        print(l)
        l[-1] += 1
    if l[0] > ((p - len(l))+1):
        return True
    else:
        for x in range(len(l)-1,-1,-1):
            if l[x] <= (n-(len(l)-(x+1))):
                continue
            else:
                l[x] += 1
                break
        backtrack(l,p)
        

backtrack(data,n)
