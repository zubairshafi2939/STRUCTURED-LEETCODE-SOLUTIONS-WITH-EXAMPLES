n = 4
p = [["."]*(n)] * (n)
def backtrack(x,l):
    
    for i in range(n):
        t = i
        tx = x
        switch = True
        while tx >=0:
            if l[tx][i] == "Q":
                switch = False
                break
            tx -=1
        tx = x
        while tx >=0 and t >= 0:
            if l[tx][t] == "Q":
                switch = False
                break
            tx -= 1
            t -= 1
        tx = x
        t = i
        while tx < n and t < n:
            if l[tx][t] == "Q":
                switch = False
                break
            tx += 1
            t += 1
        if switch == False:
            return False
        else:
            if x == n-1:
                print("True for n")
                return True
            l[x][i] == "Q"
            print(l[x][i])
            if (backtrack(x+1,l)) == True:
                # print("True")
                rest.append(l)
                return True
            else:
                l[x][i] == "."
                return False


        
rest = []
for x in range(n):
    l = list(p)
    if(backtrack(x,l)) == True:
        rest.append(l)
print(rest)
