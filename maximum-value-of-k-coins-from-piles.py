class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n=len(piles)
        for i in range(n):
            for j in range(1,len(piles[i])):
                piles[i][j]+=piles[i][j-1]
        
        @cache
        def findMax(index,k):
            if index>=n or k<=0:
                return 0

            take=0
            for i in range(min(k,len(piles[index]))):
                curr=piles[index][i]     
                take=max(take,findMax(index+1,k-(i+1))+curr)
            skip=findMax(index+1,k)
            return max(take,skip)
        
        return findMax(0,k)