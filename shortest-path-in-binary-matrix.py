class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        def check(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))
        
        queue=deque([(0,0)])
        if grid[0][0]==1:
            return -1
        else:
            grid[0][0]=1
        result=1

        while queue:
            l=len(queue)
            for _ in range(l):
                row,col=queue.popleft()

                if row==len(grid)-1 and col==len(grid[0])-1:
                    return result
                
                for vert,horz in direction:
                    new_row=row+vert
                    new_col=col+horz 
                    if check(new_row,new_col) and grid[new_row][new_col]==0:
                        grid[new_row][new_col]=1
                        queue.append((new_row,new_col))
            result+=1
        return -1