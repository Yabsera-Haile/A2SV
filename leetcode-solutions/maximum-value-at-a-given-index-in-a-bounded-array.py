class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        def check(x):
            y = max(0, x - index)
            result = (x+y) * (x-y+1) // 2
            y = max(0, x - ((n-1) - index))
            result += (x+y) * (x-y+1) // 2
            return (result - x)

        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if check(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left + 1
        