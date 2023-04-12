class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)

        seen=set()
        color=defaultdict(int)

        def dfs(vertex,prev_color):
            if not color[vertex]:
                color[vertex]=prev_color*-1
            seen.add(vertex)
            
            for adj in graph[vertex]:
                if color[adj] and color[adj]==color[vertex]:
                    return False
                if adj not in seen:
                    curr=dfs(adj,color[vertex])
                    if not curr:
                        return curr
            return True
        
        for i in range(1,n+1):
            if i not in seen:
                color.clear()
                result=dfs(i,-1)
                if not result:
                    return False
            
        return True