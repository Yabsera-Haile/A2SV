from typing import List


from typing import List
from collections import defaultdict,deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph=defaultdict(list)
        count=defaultdict(int)
        
        for u,v in edges:
            graph[u].append(v)
            count[v]+=1
        queue=deque()
        for i in range(1,n+1):
            if count[i]==0:
                queue.append(i)
        print(queue)
        result=[]
        time=1
        while queue:
            l=len(queue)
            for _ in range(l):
                curr=queue.popleft()
                result[curr]=str(time)
                for neigh in graph[curr]:
                    count[neigh]-=1
                    if count[neigh]==0:
                        queue.append(neigh)
            time+=1
        
        return " ".join(result)
