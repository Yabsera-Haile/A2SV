class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction=[(1,0),(0,1),(0,-1),(-1,0)]

        def check(row,col):
            return (0<=row<len(board)) and (0<=col<len(board[0])) 
        def dfs(row,col):
            board[row][col]="M"
            for horz,vert in direction:
                new_row=row+vert
                new_col=col+horz
                if check(new_row,new_col) and board[new_row][new_col]=="O":
                    dfs(new_row,new_col)
        
        for i in range(len(board)):
            if i==0 or i==len(board)-1:
                for j in range(len(board[0])):
                    if board[i][j]=="O":
                        dfs(i,j)
            else:
                if board[i][0]=="O":
                    dfs(i,0)
                if board[i][len(board[0])-1]=="O":
                    dfs(i,len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="M":
                    board[i][j]="O"
                else:
                    board[i][j]="X"