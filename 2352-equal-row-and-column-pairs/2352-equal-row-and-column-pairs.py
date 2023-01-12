from collections import defaultdict,Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols=defaultdict(list)
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                cols[j].append(grid[i][j])
        cols=list(map(tuple,cols.values()))
        count_cols=dict(Counter(cols))
        
        result=0
        for row in grid:
            if tuple(row) in cols:
                count=count_cols[tuple(row)]
                result+=count
                
        return result
        