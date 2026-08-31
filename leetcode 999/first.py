class Solution(object):
    def numRookCaptures(self, board):
        def check(x,y,board):
            total = 0
            for i in range(x-1,-1,-1):
                if board[i][y] == "p":
                    total += 1
                    break
                elif board[i][y] == "B":
                    break
            for i in range(x+1,len(board)):
                if board[i][y] == "p":
                    total += 1
                    break
                elif board[i][y] == "B":
                    break
            for i in range(y-1,-1,-1):
                if board[x][i] == "p":
                    total += 1
                    break
                elif board[x][i] == "B":
                    break
            for i in range(y+1,len(board[0])):
                if board[x][i] == "p":
                    total += 1
                    break
                elif board[x][i] == "B":
                    break
            return total
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "R":
                    return check(x,y,board)
        """
        :type board: List[List[str]]
        :rtype: int
        """
        

