class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        result=0
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        match=True
        def check(row,col):
            return (0<=row<len(grid2)) and (0<=col<len(grid2[0]))
        
        def dfs(row,col):
            nonlocal match
            if grid1[row][col]!=1:
                match=False
            grid2[row][col]=0
            for vert,horz in directions:
                new_row=row+vert
                new_col=col+horz
                if check(new_row,new_col) and grid2[new_row][new_col]==1:
                    dfs(new_row,new_col)
                
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid1[i][j]==1 and grid2[i][j]==1:
                    dfs(i,j)
                    if match:
                        result+=1
                    match=True
        
        return result