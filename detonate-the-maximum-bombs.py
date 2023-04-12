class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)

        for i,[x,y,r] in enumerate(bombs):
            for j,[a,b,c] in enumerate(bombs):
                if i!=j and (((x-a)**2 + (y-b)**2)**0.5)<=r:
                    graph[i].append(j)
        seen=set()
       
        def dfs(vertex):
            curr=1
            seen.add(vertex)

            for adj in graph[vertex]:
                if adj not in seen:
                    curr+=dfs(adj)
            return curr
        
        result=0
        for i in range(len(bombs)):
            if i not in seen:
                seen.clear()
                result=max(result,dfs(i))
            
        return result