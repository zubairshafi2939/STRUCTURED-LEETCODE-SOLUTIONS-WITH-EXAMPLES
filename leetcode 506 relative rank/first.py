score = [10,3,8,9,4]
data = {}
copy = list(score)
copy.sort()
position = 1
for x in range(len(copy)-1,-1,-1):
    data[copy[x]] = position
    position += 1
print(data)
award = {1:"Gold Medal", 2:"Silver Medal", 3:"Bronze Medal"}
rest = []
for x in score:
    if data[x] in award:
        rest.append(award[data[x]])
        continue
    rest.append(data[x])
print(rest)