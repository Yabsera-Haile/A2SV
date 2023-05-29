class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo={}
        def dp(n):
            if n==0 or n==1:
                memo[n]=n
                return n
            if n not in memo:
                if n%2==0:
                    memo[n]=dp(n//2)
                else:
                    memo[n]=dp(n//2)+dp(n//2+1)         
            
            return memo[n]
        for i in range(n+1):
            dp(i)
        return max(memo.values())