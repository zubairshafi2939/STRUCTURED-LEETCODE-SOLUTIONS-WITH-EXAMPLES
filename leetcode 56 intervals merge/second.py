intervals = [[1,4],[2,3],[5,8],[6,13]]
intervals.sort(key=lambda x:x[0])
result = [intervals[0]]
for x in range(1,len(intervals)):
    if intervals[x][0] <= result[-1][1]:
        result[-1][1] = intervals[x][1] if intervals[x][1] > result[-1][1] else result[-1][1]
    else:
        result.append(intervals[x])
print(result)

