tasks = ["A","A","A","B","B","B"]
data = {}
for x in tasks:
    if x not in data:
        data[x] = 1
    else:
        data[x] += 1
n = 2
print(data)
rest = 0
while data:
    for x,y in data.items():
        if y >= 1:
            y -= 1
        else:
            continue
        rest += 1
        for i in range(n):
            perflog = set()
            for g,h in data.items():
                perflog.add(h)
                if g != x and h>= 1:
                    h -= 1
                    break
                    
        rest += n
    for x,y in data.items:
        if y <= 0:
            del data[x]
            break
                
            


    


