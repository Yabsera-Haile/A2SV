class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod=10**9+7
        memo = [[0] * (k+1) for _ in range(m+1)]
        prefix = [[0] * (k+1) for _ in range(m+1)]
        prevMemo=[[0] * (k+1) for _ in range(m+1)]
        prevPrefix= [[0] * (k+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            prevMemo[i][1] = 1
            prevPrefix[i][1] = i 
        
        for _ in range(2, n+1):
            memo = [[0] * (k+1) for _ in range(m+1)]
            prefix = [[0] * (k+1) for _ in range(m+1)]
            
            for i in range(1, m+1):
                for j in range(1, k+1):
                    memo[i][j] = (i * prevMemo[i][j]) % (10**9+7)
                    
                    if i > 1 and j > 1:
                        memo[i][j] += prevPrefix[i - 1][j - 1]
                        memo[i][j] %= (10**9+7)
                    
                    prefix[i][j] = (prefix[i - 1][j] + memo[i][j]) % (10**9+7)
            
            prevMemo = [row[:] for row in memo]
            prevPrefix = [row[:] for row in prefix]
        
        return prefix[m][k]