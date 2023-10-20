class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        result = 0
        visited = set()

        def findComponent(root):
            nonlocal result
            if root in visited:
                return 0

            visited.add(root)

            curr = values[root]
            for neigh in graph[root]:
                curr += findComponent(neigh)

            if curr % k == 0:
                result += 1
                return 0

            return curr

        findComponent(0)
        return result