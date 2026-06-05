word = "aaAbcBC"
data = set()
rest = set()
for x in word:
    data.add(x)
    if x.islower() and x.capitalize() in data:
        print("True for lower")
        rest.add(x.casefold())
    elif x.isupper() and x.casefold() in data:
        rest.add(x.casefold())
print(len(rest))


