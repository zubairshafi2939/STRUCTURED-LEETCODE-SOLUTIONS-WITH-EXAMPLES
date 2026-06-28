s = "eccer"

mid = len(s)//2
sMid = mid
if len(s)%2 != 0:
    sMid = mid+1
firstHalf = s[:mid]
secondHalf = s[sMid:]
if firstHalf == secondHalf[::-1]:
    print(True)
# 03049726205
# shehroz
for x in range(len(s)):
    firstHalf = s[0:x]
    secondHalf = s[x+1:]
    s1 = firstHalf+secondHalf
    mid = len(s1)//2
    sMid = mid
    if len(s1)%2 != 0:
        sMid += 1
    FirstHalf = s1[:mid]
    SecondHalf = s1[sMid:]
    if FirstHalf == SecondHalf[::-1]:
        print(True)




    
