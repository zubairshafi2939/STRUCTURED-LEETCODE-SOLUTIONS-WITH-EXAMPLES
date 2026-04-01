s = "hello world toward  "
ret = 0
prev = []
p = ret
for x in s:
    if x == " " and p != 0:
        prev = ret
        ret = 0
    else:
        ret+=1
    p = x
print(ret)
print(prev)

