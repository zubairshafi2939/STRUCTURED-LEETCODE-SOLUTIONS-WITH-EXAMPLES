a = "11"
b = "1"
t = 0
if len(a) > len(b):
    t = a
    a = b
else:
    t = b
rest = ""
c = 0
ti = len(t) -1
gap = len(t) - len(a)
for x in range(len(a)-1,-1,-1):
        rest = str(int(t[ti]) ^ int(a[x]) ^ c) + rest
        c = (int(t[ti]) + int(a[x]) + c) // 2  # ✅ SAHI 
        ti -= 1
for x in range(gap-1, -1,-1):
    rest = str(int(t[x]) ^ int(c)) + rest
    c = (int(t[ti]) + c) // 2  
    print(c)
# print(rest)
if c == 1:
    rest = str(c) + rest





print(rest)
