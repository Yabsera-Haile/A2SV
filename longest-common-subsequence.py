class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      #Bottom UP
      n=len(text1)
      m=len(text2)
      memo =[[0]*(m+1) for _ in range(n+1)]

      for i in range(1,n+1):
        for j in range(1,m+1):
          if text1[i-1]==text2[j-1]:
            memo[i][j]=memo[i-1][j-1]+1
          else:
            memo[i][j]=max(memo[i-1][j],memo[i][j-1])
      
      return memo[n][m]
    
      # Top Down
      # memo={}

      # def findLongestCommonSubsequence(i,j):
      #   if i<0 or j<0:
      #     return 0
      #   if (i,j) in memo:
      #     return memo[(i,j)]
      #   if text1[i]==text2[j]:
      #     memo[(i,j)]=findLongestCommonSubsequence(i-1,j-1)+1
      #   else:
      #     num1=findLongestCommonSubsequence(i-1,j)
      #     num2=findLongestCommonSubsequence(i,j-1)
      #     memo[(i,j)]=max(num1,num2)
      #   return memo[(i,j)]

      # n1=len(text1)-1
      # n2=len(text2)-1 
      # findLongestCommonSubsequence(n1,n2)
      # return memo[(n1,n2)]