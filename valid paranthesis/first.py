n = "{}[]["
p = ["(","{","["]
stk = []
dic = {"(":")","{":"}","[":"]"}
count = 0
val = 0
for x in n:
    if x in p:
        stk.append(dic[x])
        count += 1
    else:
        if len(stk) == 0 or x != stk[len(stk)-1]:
            val = max(val,count)
            count = 0
            print("someting")
        else:
            stk.pop()
            count +=1
val = max(val,count)
print(val)