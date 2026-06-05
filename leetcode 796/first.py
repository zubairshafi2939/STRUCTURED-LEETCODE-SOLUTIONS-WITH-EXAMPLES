s = "abcde"
goal = "cdeab"
for x in range(len(s)):
    s = s[1:] + s[0]
    if s == goal:
        print("True")