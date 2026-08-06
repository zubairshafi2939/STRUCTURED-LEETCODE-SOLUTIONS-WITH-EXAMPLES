s = "100"
dp = [""] * len(s)
if s[0] != "0":
    dp[0] = s[0]
sub = int(s[0])
tsum = [sub]*len(s)
for x in range(1,len(s)):
    if s[x] == "0":
        dp[x] = dp[x-1]
    else:
        dp[x] = dp[x-1] + s[x]
    sub += int(s[x])
    tsum[x] = sub
# print(tsum)
# print(dp)
result = []
queries = [[0,7],[1,3],[4,6]]
for first,second in queries:
    if first != 0:
        todel = len(dp[first-1])
        prev = tsum[first-1]
    else:
        prev = 0
        todel = len(dp[first])
    main = (dp[second][todel:])
    multiplier = tsum[second] - prev
    result.append(int(main)*multiplier)



