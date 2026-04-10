n = 2863311530
t = 1
count = 0
while t <= n:
    t = t<< 1
    count += 1
num = (n & 1)
num = 0 if num == 1 else 1
for x in range(count):
    nt = n & 1
    if nt != num:
        n = n >> 1
        num = 0 if num == 1 else 1
    else:
        print(False)
        break
