s = "a1b2"
# trying after wathcing the tutorial. because this is my first
#back tracking problem (iterative approach currently doing)

output = [""]
for i in s:
    temp = []
    for o in output:
        if i.isalpha():
            temp.append(o+i.upper())
            temp.append(o+i.lower())
        else:
            temp.append(o+i)
    output = temp
print(output)
