class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={i:i for i in range(n)}

        def rep(x):
            if x==graph[x]:
                return x
            x=graph[x]
            curr=rep(x)
            graph[x]=curr
            return curr
        
        for u,v in edges:
            parentU=rep(u)
            parentV=rep(v)

            if parentU!=parentV:
                graph[parentV]=parentU    

        return rep(source)==rep(destination)