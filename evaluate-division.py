class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        nodes=set()
        for i in range(len(equations)):
            a,b=equations[i]
            graph[a].append((b,values[i]))
            graph[b].append((a,(1/values[i])))
            nodes.add(a)
            nodes.add(b)
        n=len(nodes)
        result=[]

        for a,b in queries:
            if a not in nodes or b not in nodes:
                result.append(-1)
                continue

            ans={node:inf for node in nodes}
            ans[a]=1
            visited=set()
            heap=[(1,a)]
            while heap:
                curr_value, node = heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for neigh, score in graph[node]:
                    if ans[neigh] > curr_value*score:
                        ans[neigh] = curr_value*score
                        heappush(heap, (ans[neigh], neigh))
                       
            if ans[b]==inf:
                result.append(-1)
            else:
                result.append(ans[b])


        return result