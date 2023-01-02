class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row={}
        col={}
        col_length=len(grid[0])
        row_length=len(grid)
        for i,grd in enumerate(grid):
            row[i]=sum(grd)
            for j,cell in enumerate(grd):
                col[j]=col.get(j,0)+cell
        result=[]
        print(row)
        print(col)
        for i in range(len(grid)):
            sub=[]
            for j in range(col_length):
                current=((2*col[j])-row_length)+((2*row[i])-col_length)
                sub.append(current)
            result.append(sub)
        return result
                
            
                
            
        