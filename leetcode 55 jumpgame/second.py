nums = [1,0,1,0]
# i am thinking from the left side and har aik ka max check kar kyaa hi atta hai
# implementing
high = 0
for x in range(len(nums)):
    high = max(high, x + nums[x])
    if nums[x] == 0 and high <= x:
        if x == len(nums) - 1:
            print("True")
        else:
            print("False")


