class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph=defaultdict(list)
        incoming=[0]*n

        for prev,nxt in relations:
            graph[prev-1].append(nxt-1)
            incoming[nxt-1]+=1
        
        @cache
        def findSemesters(seen):
            if not seen:
                return 0
            
            courses = [i for i in range(n) if incoming[i] == 0 and seen & 1<<i]   

            result = inf
            for combo in combinations(courses,min(k,len(courses))):
                new_seen = seen                
                for course in combo:
                    new_seen ^= 1<<course
                    for neigh in graph[course]:
                        incoming[neigh]-=1
                
                result = min( result, 1 + findSemesters(new_seen) )
                
                for course in combo:
                    for neigh in graph[course]:
                        incoming[neigh]+=1                
            return result
                
        return findSemesters((1<<n) -1)