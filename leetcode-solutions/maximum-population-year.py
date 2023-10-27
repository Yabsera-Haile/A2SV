class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop=[0]*101
        
        for log in logs:
            pop[log[0]-1950]+=1
            pop[log[1]-1950]-=1
        
        maxi=pop[0]
        result=0
        
        for i in range(1,len(pop)):
            pop[i]+=pop[i-1]
            
            if pop[i]>maxi:
                result=i
                maxi=pop[i]
        # print(pop)
        return result+1950
            
            

        