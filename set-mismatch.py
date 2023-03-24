class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        miss=sum(range(1,len(nums)+1))
        dup=sum(nums)

        for num in list(set(nums)):
            miss-=num
            dup-=num
        
        return [dup,miss]