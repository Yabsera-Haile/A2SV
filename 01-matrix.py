class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        def check(row,col):
            return (0<=row<len(mat)) and (0<=col<len(mat[0]))

        result=[[0]*len(mat[i]) for i in range(len(mat))]
        queue=deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    result[i][j]=10**4

        count=0
        while queue:
            l=len(queue)

            for _ in range(l):
                row,col=queue.popleft()
                if mat[row][col]==1:
                    result[row][col]=min(result[row][col],count)
                    
                for vert,horz in direction:
                    new_row=row+vert
                    new_col=col+horz

                    if check(new_row,new_col) and result[new_row][new_col]>count and mat[new_row][new_col]==1:
                        queue.append((new_row,new_col))
            count+=1
        
       
        return result