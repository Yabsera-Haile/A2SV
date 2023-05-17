class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph={i:i for i in range(1,len(edges)+1)}
        result=[]
        def rep(x):
            if x==graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr

        for a,b in edges:
            parentA=rep(a)
            parentB=rep(b)

            if parentA!=parentB:
                graph[parentB]=parentA
            else:
                result=[a,b]
        
        return result