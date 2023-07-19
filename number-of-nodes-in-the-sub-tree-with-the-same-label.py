class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        result = [0] * n

        def dfs(vertex, parent, count):
            prev = count[labels[vertex]]

            for neighbors in graph[vertex]:
                if neighbors != parent:
                    dfs(neighbors, vertex, count)

            count[labels[vertex]] += 1
            result[vertex] = count[labels[vertex]] - prev

        dfs(0, 0, Counter())
        return result