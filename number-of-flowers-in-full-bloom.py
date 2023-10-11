class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n=len(flowers)
        starts=[flowers[i][0] for i in range(n)]
        ends=[flowers[i][1] for i in range(n)]
        starts.sort()
        ends.sort()
        
        result=[]
        for person in people:
            start=bisect_right(starts,person)
            end=bisect_left(ends,person)
            
            result.append(start-end)
        
        return result