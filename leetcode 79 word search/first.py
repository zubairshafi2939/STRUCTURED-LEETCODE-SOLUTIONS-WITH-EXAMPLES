board = [
["A","C","C","E"],
["S","C","D","D"],
["A","D","E",""]]
word = "ACCDC"
i , j = 0,0
t = 0
def backtrack(x,y,t,L = []):
    L.append([x,y])
    if t == len(word) :
        print(True, "As fuck")
        print(L)
        return True
    if x+1 < len(board) and [x+1,y] not in L and board[x+1][y] == word[t]:
        backtrack(x+1,y,t+1)
    if y+1 < len(board[0]) and [x,y+1] not  in L and board[x][y+1] == word[t]:
        backtrack(x,y+1,t+1)
    if x-1 >=0 and [x-1,y] not in L and board[x-1][y] == word[t]:
        backtrack(x-1,y,t+1)
    if y-1 >=0 and [x,y-1] not in L and board[x][y-1] == word[t]:
        backtrack(x,y-1,t+1)
    L.pop()
    


for x in range(len(board)):
    for y in range(len(board[x])):
        if board[x][y]== word[t]:
            backtrack(x,y,t+1)
            



#and((x+1 < len(board) and board[x+1][y] == word[t])or( y+1 < len(board[0]) and board[x][y+1] == word[t])or(x-1 >=0 and board[x-1][y] == word[t])or(y-1 >=0 and board[x][y-1] == word[t]))