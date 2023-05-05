class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        heap = []
        for key , value in count.items():
            heappush(heap , [-value , key])
        result=[]
        for _ in range(k):
            value , key = heappop(heap)
            result.append(key)

        return result