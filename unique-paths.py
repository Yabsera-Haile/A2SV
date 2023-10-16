class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Combinatorics
        total=m+n-2
        return factorial(total)//(factorial(total-(m-1)) * factorial(m-1))
        
        # DP
        # memo=defaultdict(int)
        # memo[(m-1,n-1)]=1

        # def check(row,col):
        #     if 0<=row<m and 0<=col<n:
        #         return memo[(row,col)]
        #     return 0
        
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         memo[(i,j)]+=check(i+1,j)+check(i,j+1)
        
        # return memo[(0,0)]