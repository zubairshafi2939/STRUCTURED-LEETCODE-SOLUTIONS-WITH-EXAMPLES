text = "lloo"
data = {"b":0, "a":0, "l":0, "o":0, "n":0}
for x in text:
    if x in data:
        data[x] += 1
data["l"] //= 2
data["o"] //= 2
print(min(data.values()))