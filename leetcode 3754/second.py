s = " hello world "
rest = s.split()
result = ""
for x in range(len(rest)-1,-1,-1):
    if x == 0:
        result += rest[x]
        continue
    result += rest[x] + " "
print(result)