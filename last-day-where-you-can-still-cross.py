class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        graph={i:i for i in range(row*col+2)}
        board=[[1]*col for _ in range(row)]
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        
        def rep(x):
            if x==graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
        
        def check(i,j):
            return (0<=i<row) and (0<=j<col)
        result=len(cells)-1
        for i,cell in enumerate(cells[::-1]):
            _row=cell[0]-1
            _col=cell[1]-1
            board[_row][_col]=0
            parentA=rep((_row*col)+_col+1)
            for vert,horz in directions:
                new_row=_row+vert
                new_col=_col+horz
                if check(new_row,new_col) and board[new_row][new_col]==0:
                    parentB=rep((new_row*col)+new_col+1)
                    if parentA!=parentB:
                        graph[parentB]=parentA

            if _row==0:
                graph[parentA]=rep(0)
            elif _row==row-1:
                graph[parentA]=rep(row*col+1)
            # print(graph,((_row*col)+_col+1),cell)
            if rep(0) == rep(row*col+1):
                return result
            result-=1