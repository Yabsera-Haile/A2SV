class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        directions=[(1,0),(0,1),(0,-1),(-1,0)]

        def check(row,col):
            return (0<=row<n) and (0<=col<m) and grid[row][col]

        result=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    curr=4
                    for vert,horz in directions:
                        row=i+vert
                        col=j+horz
                        if check(row,col):
                            curr-=1
                    result+=curr
        
        return result
        