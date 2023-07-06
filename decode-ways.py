class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo=[0] * (n+1)
        memo[0]=memo[1]=1
        if s[0] == '0': 
            return 0

        for i in range(2, n+1):
            curr = int(s[i-1:i])
            if curr >= 1 and curr < 10:
                 memo[i] += memo[i-1]

            curr = int(s[i-2: i])
            if curr > 9 and curr <= 26: 
                memo[i] += memo[i-2]

        return memo[-1]