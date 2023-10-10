class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)

        for _from,_to,price in flights:
            graph[_from].append((_to,price))
        
        costs=[inf]*n
        costs[src]=0

        queue=deque([(src,0)])
        stops=0

        while queue:
            if stops > k:
                break

            l=len(queue)
            for _ in range(l):
                node,curr_price=queue.popleft()
                
                for neigh,price in graph[node]:
                    if costs[neigh]>curr_price+price:
                        costs[neigh]=curr_price+price
                        queue.append((neigh,costs[neigh]))
            stops+=1
        
        return costs[dst] if costs[dst] != inf else -1