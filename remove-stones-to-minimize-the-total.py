class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[piles[i]*-1 for i in range(len(piles))]
        heapify(piles)
        for _ in range(k):
            curr=heappop(piles)
            heappush(piles,curr+(-curr//2))

        return -sum(piles)