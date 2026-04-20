s = "anagram"
t = "nagarama"
data = {}
for x in s:
    if x not in data:
        data[x] = 1
    else:
        data[x] += 1
for x in t:
    if x in data and data[x] != 0:
        data[x] -= 1
    else:
        print(False)
print("True")