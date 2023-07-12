class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = -matrix[i][j]
                if len(heap) < k:
                    heappush(heap, curr)
                elif curr > heap[0]:
                    heappushpop(heap, curr)
        return -heap[0]