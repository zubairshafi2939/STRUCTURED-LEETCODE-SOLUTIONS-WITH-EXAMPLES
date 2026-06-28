nums = [-1,1,0,-3,3]
p = 1
count = 0
save = []
rest = []
for x in range(len(nums)):
    if nums[x] == 0:
        count += 1
        save.append(x)
        continue  
    p = p*nums[x]
print(p)
if count > 1:
    rest = [0] * len(nums)
elif count == 1:
    rest = [0] * len(nums)
    rest[save[0]] = p
else:
    for x in range(len(nums)):
        rest.append(int(p/nums[x]))

print(rest)