class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result=-1
        color=[0]*len(edges)
        distance={}
        graph=defaultdict(list)

        def dfs(vertex,depth):
            nonlocal result
            if color[vertex]==2:
                return
            if color[vertex]==1:
                curr=depth-distance[vertex]
                result=max(result,curr)
                return
            distance[vertex]=depth
            color[vertex]=1
            
            if edges[vertex]!=-1:
                dfs(edges[vertex],depth+1)
            
            color[vertex]=2
        
        for i in range(len(edges)):
            if color[i]==0:
                dfs(i,0)
        return result