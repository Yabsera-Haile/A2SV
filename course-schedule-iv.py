class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Floyd-Warshall's Elegance
        preq=[[inf]*numCourses for _ in range(numCourses)]

        for a,b in prerequisites:
            preq[a][b]=1
        
        for i in range(numCourses):
            preq[i][i]=0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    preq[i][j]=min(preq[i][j],preq[i][k]+preq[k][j])
        
        result=[]

        for a,b in queries:
            if preq[a][b]==inf:
                result.append(False)
            else:
                result.append(True)
        return result


        # BFS
        # graph=defaultdict(list)
        # for a,b in prerequisites:
        #     graph[a].append(b)

        # prereq=[[False]*numCourses for _ in range(numCourses)]
        
        # for i in range(numCourses):
        #     queue=deque([i])  
        #     seen=set([i])   
        #     while queue:
        #         curr=queue.popleft()
        #         prereq[i][curr]=True
        #         for neigh in graph[curr]:
        #             if neigh not in seen:
        #                 seen.add(neigh)
        #                 queue.append(neigh)     

        # result=[]
        # for i,j in queries:
        #     result.append(prereq[i][j])
        # return result