class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        size=len(piles)
        
        start=size//3
        result=0
        for index in range(start,size,2):
            result+=piles[index]
        return result
            
        
        