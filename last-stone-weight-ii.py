class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        memo={}

        def findCombo(index,_sum):
            if (index,_sum) in memo:
                return memo[(index,_sum)]
            if index==n:
                if _sum>=0:
                    return _sum
                else:
                    return inf
            memo[(index,_sum)]=min((findCombo(index+1,_sum+stones[index]),
            findCombo(index+1,_sum-stones[index])))
            return memo[(index,_sum)]
        
        return findCombo(0,0)