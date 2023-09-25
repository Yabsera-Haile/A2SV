class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n=len(dungeon)
        m=len(dungeon[0])
        memo=[[inf]*(m+1) for _ in range(n+1)]
        memo[n-1][m]=memo[n][m-1]=1

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                memo[i][j] = max(min(memo[i+1][j], memo[i][j+1]) - dungeon[i][j], 1)
            # print(memo)
                
        return memo[0][0]