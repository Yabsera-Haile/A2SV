class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = 0
        def backtrack(i, bitmask, length):
            nonlocal result
            result = max(result, length)
            if i == len(arr):
                return

            prev = bitmask
            for ch in arr[i]:
                if 1 << (ord(ch)-ord('a')) & bitmask != 0:
                    
                    backtrack(i+1, prev, length)
                    return
                bitmask |= 1<<(ord(ch)-ord('a'))

            backtrack(i+1, prev, length)

            backtrack(i+1, bitmask, length+len(arr[i]))
            return
        backtrack(0, 0, 0)
        return result