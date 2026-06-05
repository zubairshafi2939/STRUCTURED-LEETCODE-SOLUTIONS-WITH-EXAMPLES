n = 8
k = 4
data = []
for x in range(k):
    data.append(x+1)
print(data)

def backtrack(ival,prevval,data):
    for x in range(ival, n+1):
        data[-1] = x
        print(data)
    return 
backtrack(4,8, data)
