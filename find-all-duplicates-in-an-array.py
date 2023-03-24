class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result=[]

        ref=Counter(range(1,len(nums)+1))

        for num in nums:
            ref[num]-=1
        
        for key,value in ref.items():
            if value==-1:
                result.append(key)
        
        return result