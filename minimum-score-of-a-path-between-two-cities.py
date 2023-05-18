class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph={i:i for i in range(1,n+1)}

        def rep(x):
            if x==graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
        
        for road in roads:
            parent1=rep(road[0])
            parent2=rep(road[1])
            if parent1 != parent2:
                graph[parent2]=parent1
        result=10**4
  
        for road in roads:
            parent1=rep(road[0])
            parent2=rep(road[1])
            if parent1 == rep(graph[1]) and parent2 == rep(graph[1]):
                result=min(result,road[2])
        
        return result