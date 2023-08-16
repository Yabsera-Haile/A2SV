class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque()
        result=[]
        for i in range(k):
            while queue and  nums[i]>=nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])

        for i in range(k,len(nums)):
            if queue and queue[0] == i-k:
                queue.popleft()
            
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            result.append(nums[queue[0]])
        
        return result