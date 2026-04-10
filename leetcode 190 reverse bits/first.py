n = 43261596
t = 1<< 31
sum = 0
for x in range(32):
    rest = n & 1
    sum = sum + (rest * t)
    t = t >> 1
    n = n >> 1
print(sum)

