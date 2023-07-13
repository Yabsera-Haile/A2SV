class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        m, n = len(grid), len(grid[0])
        visited_state = [[set() for _ in range(n)] for _ in range(m)] 
        key = 0
        starti, startj = -1, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] in 'abcdef':
                    key += 1
                if grid[i][j] == '@':
                    starti, startj = i, j

        key_final_state = 0
        for i in range(key):
            key_final_state ^= 1 << i

        step = 0

        queue = collections.deque()  
        queue.append([starti, startj, 0, 0])

        while queue:

            for _ in range(len(queue)):

                i, j, key_state, unlocked_state = queue.popleft()

                if key_state == key_final_state:
                    return step

               
                for ii, jj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni, nj = i + ii, j + jj

                    if not (0 <= ni < m and 0 <= nj < n) or grid[ni][nj] == '#': 
                        continue
                    new_unlocked_state = unlocked_state
                    if grid[ni][nj] in "ABCDEF":  
                        bit_shift = ord(grid[ni][nj]) - ord("A")
                        if not (key_state & 1 << bit_shift):  
                            continue

                        new_unlocked_state |= 1 << i

                    new_key_state = key_state
                    if grid[ni][nj] in 'abcdef':  
                        bit_shift = ord(grid[ni][nj]) - ord('a')
                        new_key_state |= 1 << bit_shift

                    state = (new_key_state, new_unlocked_state)
                    if state in visited_state[ni][nj]:
                        continue
                    visited_state[ni][nj].add(state)

                    queue.append([ni, nj, new_key_state, new_unlocked_state])

            step += 1

        return -1