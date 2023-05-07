class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap=defaultdict(list)

        for num in nums:
            if heap[num-1]:
                heappush(heap[num],heappop(heap[num-1])+1)
            else:
                heappush(heap[num],1)

        for key,value in heap.items():
            if value:
                curr=heappop(value)
                if curr<3:
                    return False
        return True