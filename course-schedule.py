class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq=defaultdict(list)
        count=defaultdict(int)

        for a,b in prerequisites:
            prereq[b].append(a)
            count[a]+=1

        queue=deque()
        for num in range(numCourses):
            if count[num]==0:
                queue.append(num)
        
        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr)

            for neigh in prereq[curr]:
                count[neigh]-=1
                if count[neigh]==0:
                    queue.append(neigh)
        
        if len(result)==numCourses:
            return True
        else:
            return False