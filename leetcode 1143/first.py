text1 = "ABCBDE"
text2 = "BACDBD"
if (len(text1) < len(text2)):
    small = text1
    large = text2
else:
    small = text2
    large = text1
index = 0
data = set(small)
rest = []
for x in large:
    if x in data:
        rest.append(x)
print(rest)

