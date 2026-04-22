
path = "/home//doc/..///"
s = path
slash = []
for x in range(len(path)):
    if path[x] == "/":
        slash.append(x)
print(slash)

rest = ""
for x in range(len(slash)-1, 0, -1):
    if (slash[x] - slash[(x-1)]) == 1:
        slash[x] = slash[x] * -1
for x in range(1,len(slash)):
    if slash[x-1] < 0:
        print("True for: ", slash[x-1])
        val = abs(slash[x-1])+1
        rest = rest + path[val:slash[x]]
        print(path[val:slash[x]])
    elif slash[x] < 0:
        val = abs(slash[0])
        rest = rest + path[slash[x-1]:val]
    else:
        rest = rest + path[slash[x-1]:slash[x]]
print(rest)

print(slash)
# n = len(slash) - 1
# print(path[slash[n-1]+1:slash[n]])
# print(path[slash[n-2]+1:slash[n-1]])
# print(path[slash[n-3]+1:slash[n-2]])
# print(path[slash[n-4]+1:slash[n-3]])