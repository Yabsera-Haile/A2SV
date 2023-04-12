class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result=[]
        goal=len(graph)-1

        def dfs(vertex,path):
            if vertex==goal:
                result.append(path[::])
            else:
                for adj in graph[vertex]:
                    path.append(adj)
                    dfs(adj,path)
                    path.pop()
        
        dfs(0,[0])
        return result