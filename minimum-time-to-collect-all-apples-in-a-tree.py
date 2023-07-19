class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)       

        def dfs(node, parent):            
            result = 0

            for child in graph[node]:
                if child != parent:
                    result += dfs(child,node)      

            if hasApple[node] and node != 0:
                hasApple[parent] = True
                return result+2

            return result     


        return dfs(0,0)