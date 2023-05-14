class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)

        prereq=[[False]*numCourses for _ in range(numCourses)]
        
        for i in range(numCourses):
            queue=deque([i])  
            seen=set([i])   
            while queue:
                curr=queue.popleft()
                prereq[i][curr]=True
                for neigh in graph[curr]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append(neigh)     

        result=[]
        for i,j in queries:
            result.append(prereq[i][j])
        return result