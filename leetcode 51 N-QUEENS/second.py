n = 4
p = []
for x in range(n):
    resty = []
    for y in range(n):
        resty.append(".")
    p.append(resty)
# print(p)
# print(p)
tests = 0
result = []
def backtrack(x,l,lust):
    global tests
    for temp in range(0,n):
        if x == n:
            tests += 1
            return True
        if isSafe(x,temp,l):
            l[x][temp] = "Q"
            if(backtrack(x+1,l,lust)) == True:
                print("True bhenchod")
                lust.append(0)
            l[x][temp] = "."
    return lust


def isSafe(x,y,l):
    pt = y-1
    ft = y+1
    for t in range(x-1,-1,-1):
        if l[t][y] == "Q":
            return False
        if pt >=0 and l[t][pt] == "Q":
            return False
        if ft < n and l[t][ft] == "Q":
            return False
        pt -=1
        ft += 1
    return True
backtrack(0,p,result)
print(result)
print(tests)