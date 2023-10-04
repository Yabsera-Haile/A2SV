class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        result={i:inf for i in range(1,n+1)}
        result[k]=0

        visited=set()
        priority_queue=[(0,k)]

        while priority_queue:
            source_time,source = heappop(priority_queue)

            if source in visited:
                continue
            
            visited.add(source)

            for target,time in graph[source]:
                total_time=source_time+time
                
                if total_time < result[target]:
                    result[target]=total_time
                    heappush(priority_queue,(total_time,target))
        
        for i in range(1,n+1):
            if result[i]==inf:
                return -1
        
        return max(result.values())