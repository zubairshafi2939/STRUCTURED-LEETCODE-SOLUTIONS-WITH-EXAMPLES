nums = [4,5,6,7,0,1,2]
target = 3
# just going to solution cuz i didn't get it. my way is
# to try binary search if not gotten then go through from each 
# So just came to know my approach is kinda right. just some
# mild repairs 
start = 0
end = len(nums)-1
while start < end:
    mid = start + end // 2
    if mid == target:
        print(mid)
        break
    elif nums[mid] 
