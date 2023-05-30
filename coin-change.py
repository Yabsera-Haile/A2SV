class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()
        # coins.reverse()
        memo={}
        def dp(n,index):
            state=(n, index)
            if n<0 or index>=len(coins):
                return float(inf)
            elif n==0:
                return 0
            elif state not in memo:
                take = dp(n-coins[index],index) + 1
                skip = dp(n,index+1)

                memo[state]= min(take,skip)
            
            return memo[state]
        
        result= dp(amount,0)
        if result==float(inf):
            return -1
        return result