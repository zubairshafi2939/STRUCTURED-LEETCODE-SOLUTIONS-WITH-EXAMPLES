s = "applepenapple"
wordDict = ["apple","pen"]
data = {}
for x in wordDict:
    data[x] = len(x)
print(data)
for x,y in data.items():
    print(x,y)
