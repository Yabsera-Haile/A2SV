class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue=deque()
        dep=defaultdict(list)
        count=defaultdict(int)

        for i in range(len(graph)):
            if len(graph[i])==0:
                queue.append(i)
            for j in range(len(graph[i])):
                dep[graph[i][j]].append(i)
                count[i]+=1
        
        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr)

            for neigh in dep[curr]:
                count[neigh]-=1
                if count[neigh]==0:
                    queue.append(neigh)
        
        return sorted(result)