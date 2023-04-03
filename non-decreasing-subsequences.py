class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seq = []
        result = {}
        
        def backtrack(index):
            if len(seq) > 1:
                result[tuple(seq)] = 1
                
            for i in range(index, len(nums)):                    
                if (not seq) or (nums[i] >= seq[-1]):
                    seq.append(nums[i])
                    backtrack(i+1)
                    seq.pop()
                    
        backtrack(0)
        return result.keys()