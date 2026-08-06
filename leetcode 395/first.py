s = "aaabb"
k = 3
data = {}
for x in s:
    data[x] = data.get(x,0)+1
print(data)