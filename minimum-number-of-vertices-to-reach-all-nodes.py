class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = set()
        for edge in edges:
            sources.add(edge[1])
        
        result=[]
        for i in range(n):
            if i not in sources:
                result.append(i)
        
        return result