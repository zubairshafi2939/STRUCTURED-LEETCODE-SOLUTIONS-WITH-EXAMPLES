intervals = [[1,4],[4,5]]
intervals.sort(key=lambda x: x[0])
result = [[-1,-1]]
for x in range(len(intervals)-1):
    if intervals[x+1][0] <= intervals[x][1]:
        result.append([intervals[x][0],intervals[x+1][1] if intervals[x+1][1] > intervals[x][1] else intervals[x][1]])
    elif intervals[x][1] != result[-1][1]:
        result.append(intervals[x])
if intervals[-1][1] != result[-1][1]:
    result.append(intervals[-1])
result.pop(0)
print(result)



