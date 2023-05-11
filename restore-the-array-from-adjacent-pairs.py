class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        count=defaultdict(int)     
        result=[]
        seen=set()

        for u,v in adjacentPairs:
            graph[v].append(u)
            graph[u].append(v)
            count[v]+=1
            count[u]+=1
        # print(count)
        def dfs(vertex):
            result.append(vertex)
            seen.add(vertex)

            for neigh in graph[vertex]:
                if neigh not in seen:
                    dfs(neigh)
        
        for key,value in count.items():
            if value==1:
                dfs(key)
                return result