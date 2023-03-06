class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        temp=min(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if nums[i]<temp:
                return True
            else:
                while stack and stack[-1]<nums[i]:
                    temp=max(temp,stack.pop())
            stack.append(nums[i])
        
        return False