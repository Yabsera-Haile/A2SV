class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        def check(row,col):
            return (0<=row<len(board)) and (0<=col<len(board[0]))
        
        def dfs(row,col):
            count=0
            for vert,horz in directions:
                new_row=row+vert
                new_col=col+horz
                if check(new_row,new_col) and board[new_row][new_col]=='M':
                    count+=1
            if count==0:
                board[row][col]='B'
                for vert,horz in directions:
                    new_row=row+vert
                    new_col=col+horz
                    if check(new_row,new_col) and board[new_row][new_col]=='E':
                        dfs(new_row,new_col)
            else:
                board[row][col]=str(count)
        
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
        else:
            dfs(click[0],click[1])
        
        return board