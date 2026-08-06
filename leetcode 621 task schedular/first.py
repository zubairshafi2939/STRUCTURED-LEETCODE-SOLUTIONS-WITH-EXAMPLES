tasks = ["A","A","A","B","B","B"]
n = 2
words = []
data = {}
count = 0
for x in tasks:
    if x not in data:
        data[x] = 1
        words.append(x)
    else:
        data[x] += 1
rest = 0
while len(words) >= 1:
    i = 0
    x = 0
    while x < len(words) and i <= n and words:
        if data[words[x]] >= 1:
            rest += 1
            data[words[x]] -= 1
            x += 1
            i += 1
        else:
            words.pop(0)
print(rest)
        
