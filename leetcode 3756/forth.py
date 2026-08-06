s = "10203004"
queries = [[0,7],[1,3],[4,6]]
dp = [0] * (len(s)+1)
prefix = [0] * (len(s)+1)
solved = ""
words = 0
total = 0
for x in range(len(s)):
    dp[x] = words
    prefix[x] = total
    if s[x] != '0':
        solved += s[x]
        words += 1
        total += int(s[x])
dp[-1] = words
prefix[-1] = total
result = []
for first,second in queries:
    start = dp[first]
    end = dp[second+1]
    main = solved[start:end]
    total = prefix[second+1]-prefix[first]
    if main == "":
        result.append(0)
    else:
        result.append((main*total)%1000000007)
    

