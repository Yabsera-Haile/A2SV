class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]
        memo = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        memo[0][row][column] = 1

        def check(row,col):
            return ((0 <= row < n) and (0 <= col < n))

        for i in range(1, k + 1):
            for row in range(n):
                for col in range(n):
                    for horz,vert in directions:
                        prev_row, prev_col = row - horz, col - vert
                        if check(prev_row,prev_col):
                            memo[i][row][col] += memo[i - 1][prev_row][prev_col]
                    
                    memo[i][row][col] /= 8
        result=0

        for i in range(n):
            for j in range(n):
                result+=memo[k][i][j]
        
        return result