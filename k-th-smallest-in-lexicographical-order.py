class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        result = 1
        k -= 1
        while k > 0:
            steps = self.findSteps(n, result, result+1)
            if steps <= k:
                result += 1
                k -= steps
            else:
                result *= 10
                k -= 1
                
        return result

    def findSteps(self, n, n1, n2):
        steps = 0
        while n1 <= n:
            steps += min(n+1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps