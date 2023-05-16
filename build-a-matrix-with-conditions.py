class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def bfs(condition):
            graph=defaultdict(list)
            count=[0] * k

            for a,b in condition:
                graph[a].append(b)
                count[b-1]+=1
            
            queue=deque()
            for index,value in enumerate(count):
                if value==0:
                    queue.append(index+1)
            result=[]
            # print(count)
            while queue:
                curr=queue.popleft()
                result.append(curr)
                for neigh in graph[curr]:
                    count[neigh-1]-=1
                    if count[neigh-1]==0:
                        queue.append(neigh)
            
            return result

        rows=bfs(rowConditions)
        cols=bfs(colConditions)
        # print(rows,cols)
        if len(rows)<k or len(cols)<k:
            return []

        result=[[0]*k for _ in range(k)]
        
        for i,value in enumerate(rows):
            j=cols.index(value)
            result[i][j]=value
        
        return result