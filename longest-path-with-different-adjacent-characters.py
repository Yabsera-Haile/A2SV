class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        result=0
        graph=defaultdict(list)

        for i, par in enumerate(parent):
            graph[par].append(i)


        def dfs(vertex):
            nonlocal result
            first=second=0

            for neigh in graph[vertex]:
                temp=dfs(neigh)
                if s[vertex]!=s[neigh]:
                    if temp>first:
                        second=first
                        first=temp
                    elif temp>second or temp==first:
                        second=temp

            result=max(result,first+second+1)
            return first+1
        dfs(0)
        return result