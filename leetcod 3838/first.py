words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
rest = []
res = ""
for x in words:
    total = 0
    for y in x:
        word = ord(y)-97
        total += weights[word]
    res += chr(96+(26-(total%26)))
