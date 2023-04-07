class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count=defaultdict(int)
        network=set()
        for road in roads:
            count[road[0]]+=1
            count[road[1]]+=1
            network.add(tuple(road))
        
        result=0
        
        for i in range(n):
            for j in range(i+1,n):
                curr=count[i]+count[j]
                if (i,j) in network or (j,i) in network:
                    curr-=1
                result=max(result,curr)
        
        return result