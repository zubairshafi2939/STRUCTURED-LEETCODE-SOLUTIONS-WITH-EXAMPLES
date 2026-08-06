# nums = [2,34,5,6]
# print(nums[])
# num2 = '1243'
# n = 0
# for x in num2:
#     n *= 10
#     n += (ord(x) - 48)
# print(n)
n = 623
s = ''
while True:
    if n <=9:
        s = (chr(n+48)) + s
        break
    temp = n % 10
    n = n // 10
    s =  (chr(temp+48)) + s
print(s)

# s = chr(48)
# print(s)

# print(ord(num2))