class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        graph=list(range(n))
        def find( x):
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]

        def union( x, y):
            parent1 = find(x)
            parent2 = find(y)
            graph[parent1] = parent2
        
        result=[]

        for x,y in requests:
            parentX=find(x)
            parentY=find(y)
            flag=True

            for a,b in restrictions:
                parentA=find(a)
                parentB=find(b)

                if set([parentA,parentB]) == set([parentX,parentY]):
                    flag=False
                    break
            result.append(flag)
            if flag:
                union(x,y)

        return result