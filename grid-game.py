class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        result=float("inf")
        topSum = sum(grid[0])
        bottomSum = 0

        for i in range(len(grid[0])):
            topSum -= grid[0][i]
            result = min(result, max(topSum, bottomSum))
            bottomSum += grid[1][i]

        return result