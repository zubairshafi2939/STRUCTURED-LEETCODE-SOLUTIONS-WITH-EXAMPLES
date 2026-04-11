from collections import deque
nums = [2,3,4,5,3,2]
k = 3
d = deque()
right = k
rest = []
for i in range(len(nums)):
    while d and (nums[d[-1]] < nums[i] ):
        d.pop()
    d.append(i)
    if d[0] < i-k +1:
        d.popleft()
    if i >= k-1:
        rest.append(nums[d[-1]])
print(rest)