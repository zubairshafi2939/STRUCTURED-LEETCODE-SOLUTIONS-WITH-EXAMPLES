s = "aa"
end = len(s)-1
while s[end] == " ":
    end -= 1
print(end)
start = end
while start >=0 and s[start] != " " :  #while  s[start] != " " : at first i had used this. but 
    start -= 1
print(start)
print(end - start)