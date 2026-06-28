def isPalindrome(s,skip):
    l = 0
    r = len(s)-1
    condition = True
    while l<=r:
        if l == skip:# i forgot first to split
            l += 1
        if r == skip:
            r -= 1
            continue
        if s[l] != s[r]:
            condition = False
            break
        l += 1
        r -= 1
    return condition

s = "abcba"
if isPalindrome(s,-1):
    return True
for x in range(len(s)):
    if isPalindrome(s,x):
        return True
return False

