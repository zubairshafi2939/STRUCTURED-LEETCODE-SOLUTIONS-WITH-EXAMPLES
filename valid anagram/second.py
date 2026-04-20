s = "anagram"
t = "nagaram"
data = {}
for x,y in zip(s,t):
    if x not in data:
        data[x] = 1
    else:
        data[x] += 1
    if y not in data:
        data[y] = -1
    else:
        data[y] -=1
for x in data.values():
    if x != 0:
        print(False)
print(True)
print(data)