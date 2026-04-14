haystack = "sadbutsad"
needle = "sadi"

for i in range(len(haystack)):
    if haystack[i] == needle[0]:
        temp = i
        for x in range(len(needle)):
            if temp >= len(haystack):
                print("False")
                break
                # return -1
            if haystack[temp] != needle[x]:
                print(False)
                break
            else:
                temp+=1
print("True")