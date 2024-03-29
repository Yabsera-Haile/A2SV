class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n+1)
        memo[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                memo[i] += memo[j] * memo[i-j-1]

        return memo[n]