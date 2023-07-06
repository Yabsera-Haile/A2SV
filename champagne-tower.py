class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = query_row+1
        memo = [[0]*(i+1) for i in range(n)]
        memo[0][0] = poured

        for i in range(1,n):
            memo[i][0] = max(0,(memo[i-1][0] - 1)/2)
            memo[i][i] = max(0,(memo[i-1][i-1]-1)/2)
            
            for j in range(1,i):
                memo[i][j] = max(0,(memo[i-1][j-1]-1)/2) + max(0,(memo[i-1][j]-1)/2)
        
        return min(memo[query_row][query_glass],1)