class Solution(object):
    def isValidSudoku(self, board):     
        def rule1(board):
            for row in range(9):
                exist = {}
                for col in range(9):
                    if board[row][col]!=".":
                        if exist.get(int(board[row][col])-1,-1) != -1:
                            return False
                        else:
                            exist[int(board[row][col])-1] = 1
            return True

        def rule2(board):
            for row in range(9):
                exist = {}
                for col in range(9):
                    if board[col][row]!=".":
                        if exist.get(int(board[col][row])-1,-1) != -1:
                            return False
                        else:
                            exist[int(board[col][row])-1] = 1
            return True

        def rule3(board):
            for row in range(0,9,3):
                for col in range(0,9,3):
                    l = [0]*9
                    for x in range(row,row+3):
                        for y in range(col,col+3):
                            if board[x][y]!=".":
                                if l[int(board[x][y])-1] == 1:
                                    return False
                                else:
                                    l[int(board[x][y])-1] = 1
            return True
    
        return rule1(board) and rule2(board) and rule3(board)