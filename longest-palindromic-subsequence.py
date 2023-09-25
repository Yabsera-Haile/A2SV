class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
      n=len(s)
      text1=s
      text2=s[::-1]
      reverse=s[::-1]
      memo =[[0]*(n+1) for _ in range(n+1)]

      for i in range(1,n+1):
        for j in range(1,n+1):
          if text1[i-1]==text2[j-1]:
            memo[i][j]=memo[i-1][j-1]+1
          else:
            memo[i][j]=max(memo[i-1][j],memo[i][j-1])
      
      return memo[n][n]