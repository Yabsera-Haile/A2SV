class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        result=[]
        for row in range(n-2):
            column=[]
            for col in range(n-2):
                _max=0
                for i in range(3):
                    for j in range(3):
                        _max=max(_max,grid[i+row][j+col])
                column.append(_max)
            result.append(column)
        return result
                
                            
        