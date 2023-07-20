class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for i, nodes in enumerate(routes):
            for node in nodes:
                graph[node].add(i)

        result = -1
        visited = set()
        queue = deque()
        queue.append(source)

        while queue:
            l = len(queue)
            result += 1
            for _ in range(l):
                curr = queue.popleft()
                if curr == target:
                    return result

                for bus in graph[curr]:
                    if bus not in visited:
                        visited.add(bus)
                        queue.extend(routes[bus])
        return -1