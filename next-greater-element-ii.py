class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        result=[-1]*len(nums)

        for i,num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                result[stack.pop()]=num
            stack.append(i)
        
        for i,num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                result[stack.pop()]=num
                
        return result