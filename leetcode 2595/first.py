n = 50
t = 1
nums = [0,0]
i = 0
while t < 50:
    rest = n & 1
    if rest:
        nums[i] = nums[i] +1
    t = t << 1
    n = n >> 1
    i += 1
    if i >1:
        i = 0
    print("True")
print(nums)
