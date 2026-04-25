nums = [2,3,4,5,7,8,5,3]
nm = set(nums)
longest = 0
for n in nm:
    if (n-1) not in nm:
        length = 1
        while n + length in nm:
            length += 1
        longest = max(longest, length)
print(longest)