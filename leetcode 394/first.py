s = "1[1[p]1[1[j]]]"
i = 0
def backtrack(startPoint,digit,s):
    temp = ""
    while s[startPoint] != "]":
        if s[startPoint].isdigit():
            tempDigit = ""
            while s[startPoint].isdigit():
                tempDigit += s[startPoint]
                startPoint += 1
                if s[startPoint] == "[":
                    reqiured = backtrack(startPoint+1,int(tempDigit),s)
                    startPoint = reqiured[1]
                    temp += reqiured[0]
                    break
        else:            
            temp += s[startPoint]
            startPoint += 1
    return [temp*digit,startPoint+1]
result = ""
while i < len(s):
    if s[i].isdigit():
        digit = ""
        while s[i].isdigit():
            digit += s[i]
            i += 1
            if s[i] == "[":
                required = backtrack(i+1,int(digit),s)
                i = required[1]
                result += required[0]
                break
    else:
        result += s[i]
        i += 1
print(result)
        
    
