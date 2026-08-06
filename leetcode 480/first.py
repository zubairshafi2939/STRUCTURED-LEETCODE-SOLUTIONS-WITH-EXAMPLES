nums = [1,4,2,3]
k = 4
end = k
first = k//2
second = first-1
half = k//2
rest = []
for x in range(len(nums)-(k-1)):
    data = nums[x:end]
    data.sort()
    end += 1
    if k%2 != 0:
        rest.append(float(data[half]))
    else:
        result = (data[first]+data[second])/2
        rest.append(result)
print(rest)