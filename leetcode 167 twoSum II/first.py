numbers = [3,24,50,79,88,150,345]
target = 9
left = 0
right = 1
while right<len(numbers):
    value = numbers[left] + numbers[right]
    if value == target:
        print(left,right)
        break
    if value > target or (right == len(numbers)-1):
        left += 1
    else:
        right += 1