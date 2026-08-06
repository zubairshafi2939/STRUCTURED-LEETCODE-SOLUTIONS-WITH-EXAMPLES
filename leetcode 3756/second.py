s = "10203004"
mod = 10**9 + 7
queries = [[0,7],[1,3],[4,6]]
dp = [0]* len(s)
dp[0] = s[0] if s[0] != '0' else ""
prefix = [0]* len(s)
prefix[0] = int(s[0])
for x in range(1,len(s)):
    prefix[x] =  prefix[x-1]+ int(s[x])
    if s[x] != '0':
        dp[x] = dp[x-1] + s[x]
    else:
        dp[x] = dp[x-1]
result = []
for first,second in queries:
    below = dp[first-1]
    num = prefix[second] - prefix[first-1]
    if first == 0:
        below = ""
        num = prefix[second]
    main = dp[second]
    main = main[len(below):]
    rest = int(main)* num
    result.append(rest % mod)
print(result)


