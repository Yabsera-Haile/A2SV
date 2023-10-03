class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff=[]
        for i,cost in enumerate(costs):
            a,b=cost
            diff.append(((a-b),i))
        diff.sort()
        result=0
        n=len(costs)
        for i in range(n):
            if i<n//2:
                result+=costs[diff[i][1]][0]
            else:
                result+=costs[diff[i][1]][1]     
        
        return result