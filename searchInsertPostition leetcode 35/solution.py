nums = [2,3,5,7]
target = 0
left = 0
right = len(nums) - 1
while left<=right:
    mid = (left + right )//2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid] < target:
        left = mid + 1
    if nums[mid] > target:
        right = mid - 1
print(left)
print(right)