class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph=defaultdict(list)

        for a,b in richer:
            graph[b].append(a)

        seen=set()
        result=[0]*len(quiet)

        def dfs(vertex):
            if vertex in seen:
                return result[vertex]

            seen.add(vertex)
            curr=quiet[vertex]
            ans=vertex

            for neigh in graph[vertex]:
                temp=dfs(neigh)
                if curr>=quiet[temp]:
                    curr=quiet[temp]
                    ans=temp
            
            result[vertex]=ans
            
            return ans
        
        for i in range(len(quiet)):
            if i not in seen:
                dfs(i)
        
        return result