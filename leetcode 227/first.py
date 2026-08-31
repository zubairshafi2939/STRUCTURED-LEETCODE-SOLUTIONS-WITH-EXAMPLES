class Solution(object):
    def calculate(self, s):
        s = s.replace(" ","")
        rest = []
        x = 0
        start = 0
        while x < len(s):
            if not s[x].isdecimal():
                rest.append(int(s[start:x]))
                rest.append(s[x])
                start = x+1
            x+=1
        rest.append(int(s[start:]))
        i = 0
        while i < len(rest):
            if rest[i] == "/":
                cal = rest[i-1]//(rest[i+1])
                rest[i] = cal
                rest.pop(i-1)
                rest.pop(i)
            elif rest[i] == "*":
                cal = rest[i-1]*(rest[i+1])
                rest[i] = cal
                rest.pop(i-1)
                rest.pop(i)
            else:
                i+=1
        i = 0
        while i < len(rest):
            if rest[i] == "+":
                cal = rest[i-1]+(rest[i+1])
                rest[i] = cal
                rest.pop(i-1)
                rest.pop(i)
            elif rest[i] == "-":
                cal = rest[i-1]-(rest[i+1])
                rest[i] = cal
                rest.pop(i-1)
                rest.pop(i)
            else:
                i+=1
        i = 0
        



        return rest[0]

        """
        :type s: str
        :rtype: int
        """
        
s =  "1+2*5/3+6/4*2"
sol = Solution()
print(sol.calculate(s))

# s = "4"
# print(s.isdecimal())