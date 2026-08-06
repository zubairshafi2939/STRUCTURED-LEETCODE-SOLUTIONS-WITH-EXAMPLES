nums = [1,1,1,1,0,0,0,0,1,1,1,0,0]
count = {0:-1}
max_len = 0
score = 0
for x in range(len(nums)):
    if nums[x] == 0:
        score -= 1
    else:
        score += 1
    if score in count:
        max_len = max(max_len, x - count[score])
    else:
        count[score] = x
print(max_len)