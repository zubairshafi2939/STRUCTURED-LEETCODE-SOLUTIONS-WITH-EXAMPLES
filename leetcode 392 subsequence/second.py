s = "abc"
t = "asdfbsdkjcs"
i = 0
j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1 # why just i += 1 not j?
        # j +=1 this is wrong 
    j += 1
