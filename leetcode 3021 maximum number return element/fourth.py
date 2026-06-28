nums = [2,2,4,4,16,16,256]
result =1
mp = {}
for x in nums:
    mp[x] = mp.get(x, 0) + 1

for x in nums:
    if x == 1:
        
    if mp[x] >= 2:
        ct = 0
        curr = x
        while curr in mp:
            if mp[x] == 1:
                ct +=1
                break
            ct += 1
            curr *= curr
        result = max(result, ct*2-1)
print(result)