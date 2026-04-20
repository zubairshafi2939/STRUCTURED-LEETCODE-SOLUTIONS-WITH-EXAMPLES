nums = [2,3,-2,4,5]
sum = 1
maxi = 0
for x in nums:
    prev = sum
    sum = sum * x
    if sum < 0:
        maxi = max(prev, maxi)
        sum = 1
maxi = max(maxi, sum)
print(maxi)
