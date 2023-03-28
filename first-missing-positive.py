class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if int(nums[i])>0 and int(nums[i])<len(nums)+1:
                nums[int(nums[i])-1]=str(nums[int(nums[i])-1])
            elif isinstance(nums[i],int):
                nums[i]=i+1

        result=len(nums)+1

        for i in range(len(nums)):
            if isinstance(nums[i],int):
                result=i+1
                break

        # print(nums)
        return result