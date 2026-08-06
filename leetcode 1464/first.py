nums = [3,7]
first = -1
second = -2
third = -3
for x in nums:
    if x > first:
        temp = first
        first= x
        if temp > second:
            second = temp
        elif temp > third
    elif x <= first and x > second:
        second = x
    
print(first)
print(second)