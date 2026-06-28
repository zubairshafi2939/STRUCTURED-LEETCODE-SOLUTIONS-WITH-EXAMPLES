# first implement counting sort 
costs = [10,6,8,7,7,8]
coins = 7
sorted = [0] * (max(costs)+1)
for x in costs:
    sorted[x] +=1
order = []
sum = 0
for y in range(len(sorted)):
    for i in range(sorted[y]):
        sum += y
        if sum > coins:
            break
        order.append(y)
    if sum > coins:
        break
print(len(order))

# guessing it to be optimal approch but will do after brute force type
# for y in range(len(sorted)):
#     if sorted[y] == 0:
#         continue
#     else:
