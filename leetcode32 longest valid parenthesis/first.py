#just tried it many times on another folder now working cleanly on it
s = "(()"
#couldn't get the solution now grinding through solutions on leetcode
# and ai . after many hours and try
# after getting all the info. restarting
s = "(()))((()))"
stk = [-1]
rest = 0
for x in range(len(s)):
    if s[x] == "(":
        stk.append(x)
    else:
        stk.pop()
        if len(stk) == 0:
            stk.append(x)
        else:
            rest = max(rest, x - stk[-1])
print(rest)