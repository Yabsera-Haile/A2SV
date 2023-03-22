class Solution(object):
    def shortestSubarray(self, A, K):
        prefix = [0]
        for x in A:
            prefix.append(prefix[-1] + x)
        result = len(A)+1
        queue = deque()
        for key, value in enumerate(prefix):
            while queue and value <= prefix[queue[-1]]:
                queue.pop()
            while queue and value - prefix[queue[0]] >= K:
                result = min(result, key - queue.popleft())

            queue.append(key)

        return result if result < len(A)+1 else -1