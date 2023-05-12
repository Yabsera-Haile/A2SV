class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        group_graph=defaultdict(list)
        count=defaultdict(int)
        group_count=defaultdict(int)
        groups=defaultdict(list)

        for i in range(n):
            if group[i]==-1:
                group[i]=m
                m+=1
            groups[group[i]].append(i)

        for i in range(n):
            for item in beforeItems[i]:
                if group[i]!=group[item]:
                    group_graph[group[item]].append(group[i])
                    group_count[group[i]]+=1
                else:
                    graph[item].append(i)
                    count[i]+=1
        queue1=deque()

        for i in range(m):
            if group_count[i]==0 and len(groups[i])>0:
                queue1.append(i)
        
        result=[]
        while queue1:
            curr=queue1.popleft()
            queue2=deque()
            for num in groups[curr]:
                if count[num]==0:
                    queue2.append(num)
            while queue2:
                num=queue2.popleft()
                result.append(num)
                for neigh in graph[num]:
                    count[neigh]-=1
                    if count[neigh]==0:
                        queue2.append(neigh)
            for neigh in group_graph[curr]:
                group_count[neigh]-=1
                if group_count[neigh]==0:
                    queue1.append(neigh)
        
        if len(result)==n:
            return result
        else:
            return []