class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)

        @cache
        def findCost(index,paid):
            if index>=n:
                return 0
            if days[index]<=paid:
                return findCost(index+1,paid)
            else:
                day=findCost(index+1,days[index])+costs[0]
                week=findCost(index+1,days[index]+6)+costs[1]
                month=findCost(index+1,days[index]+29)+costs[2]

                return min(day,week,month)
        
        return findCost(0,-1)