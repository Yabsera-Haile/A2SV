class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result=0
        seen=set()
        graph=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if j!=i and isConnected[i][j]==1:
                    graph[i+1].append(j+1)     

        def dfs(vertix):
            seen.add(vertix)
            for adj in graph[vertix]:
                if adj not in seen:
                    dfs(adj)
        
        for key in range(1,len(isConnected)+1):
            if key not in seen:
                result+=1
                dfs(key)
        
        return result