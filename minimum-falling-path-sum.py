class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = [[0] * len(matrix) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            memo[0][i] = matrix[0][i]
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                curr = memo[i - 1][j]
                if j - 1 >= 0:
                    curr = min(curr, memo[i - 1][j - 1])
                if j + 1 < len(matrix):
                    curr = min(curr, memo[i - 1][j + 1])
                memo[i][j] = curr + matrix[i][j]
        return min(memo[-1])