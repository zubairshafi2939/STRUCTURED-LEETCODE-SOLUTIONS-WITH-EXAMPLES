num =  "1123581321"
def additive(second,total,ending,num):
    while ending < (len(num)):
        full = str(int(second) + int(total))
        y = ending
        ending = ending + len(full)
        if full != num[y:ending]:
            return False
        second = total
        total = full
    return True
        

for x in range(1,len(num)//2):
    if num[0]=='0' and x > 1:
        break
    for y in range(x+1,(len(num))):
        if num[x] == '0' and y > x+1:
            break
        first = (num[0:x])
        second = (num[x:y])
        total = str(int(first)+int(second))
        print(total)
        ending = len(total)+y
        if total == num[y:ending]:
            if additive(second,total,ending,num):
                print(True)
            else:
                print(False)
            

        
