nums = [1,1,1,1,0,0,0,0,1,1,1,0,0]
score = 0
maps = {0:-1}
high = 0
for i in range(len(nums)):
    if nums[i] == 0:
        score -= 1
    else:
        score += 1
    if score not in maps:
        maps[score] = i
    else:
        high = max(high, i - maps[score])
        print(high , "when index is " , i)
print(maps)
print(high)