a = "101"
b = "11"
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

if c:
    if gap >0:
        c =( c + int(t[ti]))//2
        rest = str(c) + rest
        rest = t[0:gap-1] + rest
    else:
        rest = str(c) + rest
elif gap > 0:
    rest = t[0:gap] + rest






print(rest)
