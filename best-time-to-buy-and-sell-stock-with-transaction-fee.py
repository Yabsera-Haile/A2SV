class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # BOTTOM UP
        stay=[-prices[0]]
        buy=[0]

        for i in range(1,len(prices)):
            stay.append(max(stay[-1],buy[-1]-prices[i]))
            buy.append(max(buy[-1],stay[-1]+prices[i]-fee))
        
        return buy[-1]

            



        # TOP DOWN
        # memo={}

        # def chooseStock(index,stock,_sum):
        #     if index==len(prices):
        #         return _sum
        #     state=(index,stock,_sum)
        #     if state not in memo:
        #         if stock==-1:
        #             memo[state]=max(chooseStock(index+1,index,_sum),chooseStock(index+1,stock,_sum))
        #         else:
        #             new_sum=_sum+(prices[index]-prices[stock]-fee)
        #             memo[state]=max(chooseStock(index+1,-1,new_sum),chooseStock(index+1,stock,_sum))
            
        #     return memo[state]
        
        # return chooseStock(0,-1,0)