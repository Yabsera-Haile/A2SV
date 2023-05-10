class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        count=defaultdict(int)

        for _from,_to in edges:
            graph[_from].append(_to)
            count[_to]+=1
        
        queue=deque()
        for i in range(n):
            if count[i]==0:
                queue.append(i)
        
        result=[[] for _ in range(n)]
        while queue:
            curr=queue.popleft()
            for neigh in graph[curr]:
                result[neigh].extend(result[curr])
                result[neigh].append(curr)
                count[neigh]-=1
                if count[neigh]==0:
                    result[neigh]=list(set(result[neigh]))
                    result[neigh].sort()
                    queue.append(neigh)
        
        return result