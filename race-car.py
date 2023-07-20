class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])
        while queue:
            moves, pos, speed = queue.popleft()

            if pos == target:
                return moves
            queue.append((moves + 1, pos + speed, 2 * speed)) 
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                queue.append((moves + 1, pos, -speed / abs(speed)))