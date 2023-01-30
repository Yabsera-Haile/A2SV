class Solution:
    def gridCheck(self, grid: List[List[int]]) -> int:
        current=[]
        row_sums=[]
        for row in grid:
            row_sums.append(sum(row))
            current.extend(row)
        current.sort()
        diag_sum1=grid[0][0]+grid[2][2]+grid[1][1]
        diag_sum2=grid[2][0]+grid[0][2]+grid[1][1]
        col_sums = [sum([row[i] for row in grid]) for i in range(3)]
        row_sums.extend(col_sums)
        row_sums.extend([diag_sum1,diag_sum2])
        result=len(set(row_sums))
        if result == 1 and current== list(range(1,10)):
            return True
        else:
            return False
                  
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)-2):
            for col in range(len(grid)-2):
                square = [grid[row+index][col:col+3] for index in range(3)]
                if self.gridCheck(square):
                    result += 1
        
        return result

        
            
            
                
        