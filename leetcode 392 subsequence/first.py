s = "abc"
t = "ahdc"
rest = True
for x in range(len(s)):
    i = 0
    isFound = False
    while i < len(t):
        if s[x] == t[i]:
            isFound = True
            break
        i += 1
    if isFound == False:
        rest = False
        break
print(rest)

