# doing after 3 months or more. 
s = "a1b2"
rest = []
def backtrack(sub="",i  = 0):
    if len(sub) == len(s):
        rest.append(sub)
        return
    if s[i].isalpha():
        backtrack(sub + s[i].swapcase(),i+1)
    backtrack(sub + s[i],i+1)
backtrack()
print(rest)

