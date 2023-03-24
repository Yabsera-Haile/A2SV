class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        right=len(nums)
        left=0
        result=0
        for i,num in enumerate(nums):
            if num<right and num>left:
                greater=0
                lesser=0
                for j,temp in enumerate(nums):
                    if i!=j and num==temp:
                        result=num
                        break
                    elif temp<num:
                        greater+=1
                    elif temp>num:
                        lesser+=1
                if greater>num-1:
                    right=num
                if lesser>len(nums)-num-1:
                    left=num
        
        return result