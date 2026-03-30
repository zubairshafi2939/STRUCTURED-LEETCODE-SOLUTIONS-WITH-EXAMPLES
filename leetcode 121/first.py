prices = [2,1,4]
left = 0
right = len(prices) - 1
result = 0
while left < right:
    value = prices[right] - prices[left]
    result = max(result,value)
    if prices[right] >= prices[left]:
        left += 1
    else:
        right -= 1
print(result)