class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph=defaultdict(list)
        incoming=[0]*n
        result=[time[i] for i in range(n)]

        for prev,nxt in relations:
            graph[prev-1].append(nxt-1)
            incoming[nxt-1]+=1
        
        queue=deque()
        
        for i in range(n):
            if incoming[i]==0:
                queue.append(i)
        
        while queue:
            node=queue.popleft()
            for neigh in graph[node]:
                incoming[neigh]-=1
                result[neigh]=max(result[neigh],time[neigh]+result[node])
                if incoming[neigh]==0:
                    queue.append(neigh)
            
        return max(result)