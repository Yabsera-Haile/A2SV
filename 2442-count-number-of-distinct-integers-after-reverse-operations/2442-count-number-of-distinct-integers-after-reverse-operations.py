class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result=[]
        for num in nums:
            current=int(str(num)[::-1])
            result.append(current)
        result+=nums
        return len(set(result))
            
        