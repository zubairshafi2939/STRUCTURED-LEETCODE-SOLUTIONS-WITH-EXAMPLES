gas  = [1,1,1,1,1,1,1,100]
cost = [2,2,2,2,2,2,2,86]
for x in range(len(gas)):
    if x == 0:
        gas[x] = gas[x] -  cost[x]
    else:
        gas[x] = gas[x]+gas[x-1] - cost[x]

print(gas)