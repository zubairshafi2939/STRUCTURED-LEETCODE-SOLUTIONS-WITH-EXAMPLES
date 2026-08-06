n = 10203004
temp = 1
rest = 0
tsum = 0
while n > 9:
    x = n % 10
    tsum += x
    n = n // 10
    if x == 0:
        continue
    rest += (x*temp)
    temp *= 10
rest += ((n*temp))


print(rest*tsum)
