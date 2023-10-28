class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        @cache
        def findProfit(index,flag,trans):
            if index>=n or trans<1:
                return 0

            if flag:
                return max(findProfit(index+1,not flag,trans)-prices[index],
                findProfit(index+1,flag,trans))
            else:
                return max(findProfit(index+1,not flag,trans-1)+prices[index],
                findProfit(index+1,flag,trans))
        
        return findProfit(0,True,2)