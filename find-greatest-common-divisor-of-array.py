class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def find(a,b):
            if b==0:
                return a
            return find(b,a%b)
        
        return find(max(nums),min(nums))