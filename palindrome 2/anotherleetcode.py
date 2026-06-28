stones = [2,7,4,1,8,1]
stones.sort()
last = len(stones)-1
secondLast = len(stones)-2
while secondLast >=0:
    first = stones.pop(last)
    second = stones.pop(secondLast)
    stones.append(first-second)
    last -= 1
    secondLast -=1
    stones.sort()
print(stones)