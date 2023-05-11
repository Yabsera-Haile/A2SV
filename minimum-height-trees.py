class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        count=defaultdict(int)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            count[a]+=1
            count[b]+=1
        
        queue=deque()
        for key,value in count.items():
            if value==1:
                queue.append(key)
        seen=set()
        num=n
        while queue and num>2:
            l=len(queue)
            for _ in range(l):
                curr=queue.popleft()
                seen.add(curr)
                num-=1
                for neigh in graph[curr]:
                    count[neigh]-=1
                    if count[neigh]==1:
                        queue.append(neigh)
  
        result=[]
        for i in range(n):
            if i not in seen:
                result.append(i)
        
        return result