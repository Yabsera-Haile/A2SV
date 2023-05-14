from collections import defaultdict,deque
def parallelCourses(n, prerequisites):
    # Write your code here.
    graph=defaultdict(list)
    count=defaultdict(int)
    nums=set()
    for a,b in prerequisites:
        graph[a].append(b)
        count[b]+=1

    queue=deque()
    for i in range(1,n+1):
        if count[i]==0:
            queue.append(i)

    time=0
    courses=[]
    while queue:
        l=len(queue)
        for _ in range(l):
            curr=queue.popleft()
            courses.append(curr)
            for neigh in graph[curr]:
                count[neigh]-=1
                if count[neigh]==0:
                    queue.append(neigh)
        time+=1

    if len(courses)==n:
        return time
    else:
        return -1