list1 = [1,2,4]
list2 = [1,3,4]
rest = []
while list1 or list2:
    if list1 and list2:
        if list1[0] < list2[0]:
            rest.append(list1[0])
            list1.pop(0)
        else:
            rest.append(list2[0])
            list2.pop(0)
        continue
    while list1:
        rest.append(list1[0])
        list1.pop(0)
    while list2:
        rest.append(list2[0])
        list2.pop(0)
    
print(rest)