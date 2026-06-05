num1 = 198 
num2 = 202
result = 0
for x in range(num1,num2+1):
    temp = str(x)
    if len(temp)<3:
        continue
    start = 0
    mid = 1
    end = 2
    for y in range(2,len(temp)):
        if temp[end]<temp[mid] >temp[start] or temp[end]> temp[mid] < temp[start]:
            result+= 1
        start += 1
        mid +=1 
        end += 1
print(result)





