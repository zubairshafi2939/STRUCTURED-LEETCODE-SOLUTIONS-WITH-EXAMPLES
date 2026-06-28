# MY FIRST APPROACH
# FIRST APPROACH IS DP LIKE BUT I AM ITERATING EVERYTIME SO IT IS
# On square but yes it will pass all the test case and return true
# nums = [1,2,4,2,6,1,4,0,3,8]
# dp = [99999] * len(nums)
# dp[0] = 0
# for x in range(1, len(nums)):
#     for y in range(0, x):
#         length = y + nums[y]
#         if length >= x:
#             dp[x] = min(dp[x],dp[y]+1)
# print(dp)
# Now i just need some logic so i can eliminate all the test cases 
# comes out to be not eligible
## Final submission:
## So find out that it can be done by On time complexity on my own without any video
# by checking the pattern on my register with pen. Happy to clear this on my first submission(athough it took me 2 solid days or more)