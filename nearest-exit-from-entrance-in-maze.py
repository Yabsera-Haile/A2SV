class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction=[(1,0),(0,1),(-1,0),(0,-1)]

        def check(row,col):
            return (0<=row<len(maze)) and (0<=col<len(maze[0]))
        def checkExit(row,col):
            return (0==row) or (row==len(maze)-1) or (0==col) or (col==len(maze[0])-1)
        
        maze[entrance[0]][entrance[1]]="+"
        queue=deque([(entrance[0],entrance[1],0)])

        while queue:
            row,col,dist=queue.popleft()
            
            for vert,horz in direction:
                new_row=row+vert
                new_col=col+horz

                if check(new_row,new_col) and maze[new_row][new_col]==".":
                    if checkExit(new_row,new_col):
                        return dist+1
                    maze[new_row][new_col]="+"
                    queue.append((new_row,new_col,dist+1))
        return -1