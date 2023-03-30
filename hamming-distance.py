class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result=x^y
        return result.bit_count()