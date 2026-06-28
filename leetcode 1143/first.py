text1 = "ABCBDE"
text2 = "BACDBD"
if (len(text1) < len(text2)):
    small = text1
    large = text2
else:
    small = text2
    large = text1
index = 0
rest = []
for x in small:
    for y in range(len(large)):
        if large[y] == x:
            rest.append(y)
            break
print(rest)

