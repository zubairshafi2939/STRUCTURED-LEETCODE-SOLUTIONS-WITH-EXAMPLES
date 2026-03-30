prices = [2,1,4]
left = 0
right = 1
profit = 0
while right != len(prices):
    if prices[left] < prices[right]:
        prof = prices[right] - prices[left]
        profit = max(prof,profit)
    else:
        left = right
    right += 1
print(profit)
