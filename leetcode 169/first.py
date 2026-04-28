nums = [3,3,4]
nums.sort()
n = set()
t = 1
mex = t
rest = nums[0]
for x in nums:
    if x in n:
        t += 1
    else:
        t = 1
        n.add(x)
    mex = max(t,mex)
    if mex == t:
        print(mex,t,x)
        rest = x
print(rest)
        
    


