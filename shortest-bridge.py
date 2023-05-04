class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direction=[(1,0),(0,1),(-1,0),(0,-1)]

        def check(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid))
        
        def dfs(row,col):
            grid[row][col]=2

            for horz,vert in direction:
                new_row,new_col=row+vert,col+horz
                if check(new_row,new_col) and grid[new_row][new_col]==1:
                    dfs(new_row,new_col)
        marked=False
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==1 and not marked:
                    dfs(i,j)
                    marked=True
                elif grid[i][j]==1 and marked:
                    queue.append((i,j))
        result=0
        while queue:
            l=len(queue)
            for _ in range(l):
                row,col=queue.popleft()
                for vert,horz in direction:
                    new_row,new_col=row+vert,col+horz
                    if check(new_row,new_col) and grid[new_row][new_col]==2:
                        return result
                    elif check(new_row,new_col) and grid[new_row][new_col]==0:
                        grid[new_row][new_col]=1
                        queue.append((new_row,new_col))
            result+=1