class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph={tuple(stone):tuple(stone) for stone in stones}
        def rep(x):
            if x ==graph[x]:
                return x
            curr = rep(graph[x])
            graph[x]=curr
            return curr
        
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    parentA=rep(tuple(stones[i]))
                    parentB=rep(tuple((stones[j])))
                    if parentA!=parentB:
                        graph[parentB]=parentA
        count=0
        for stone in stones:
            if tuple(stone)==rep(tuple(stone)):
                count+=1
        return len(stones)-count