class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=defaultdict(list)
        
        for  i,edge in enumerate(edges):
            a,b=edge
            graph[a].append((b,succProb[i]))
            graph[b].append((a,succProb[i]))
        
        probs={i:0 for i in range(n)}
        probs[start_node]=1

        visited=set()
        queue=[(-1,start_node)]

        while queue:
            curr_prob,node = heappop(queue)
            curr_prob*=-1
            if node in visited:
                continue
            visited.add(node)

            for neigh,prob in graph[node]:
                if probs[neigh]<curr_prob*prob:
                    probs[neigh]=curr_prob*prob
                    heappush(queue,(-probs[neigh],neigh))
        
        return probs[end_node]