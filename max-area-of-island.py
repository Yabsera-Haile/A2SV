class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction=[(1,0),(0,-1),(0,1),(-1,0)]
        def check(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))
        def dfs(row,col):
            grid[row][col]=0
            curr=1
            for vert,horz in direction:
                new_row=row+vert
                new_col=col+horz
                if check(new_row,new_col) and grid[new_row][new_col]:
                    curr+=dfs(new_row,new_col)
            return curr
        
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    result=max(result,dfs(i,j))
                    
        
        return result