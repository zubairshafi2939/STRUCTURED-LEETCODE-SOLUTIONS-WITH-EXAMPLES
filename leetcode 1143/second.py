text1 = "abcde"
text2 = "ace" 
dp = [0]*len(text1)
longest = 0

for x in range(len(text2)):
    curr_length = 0
    for y in range(len(dp)):
        if curr_length < dp[y]:
            curr_length = dp[y]
        elif text2[x] == text1[y]:
            dp[y] = curr_length+1
            longest = max(longest,curr_length+1)
print(longest)
