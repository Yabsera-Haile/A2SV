class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #initialize pointers
        pointer1=0
        pointer2=pointer1+1
        
        #iterate and check how many times val occured
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
                k+=1
                
        #move values that aren't val to the left  
        while pointer2<len(nums):
            # print(pointer1,pointer2)
            if nums[pointer1]==val and nums[pointer2]!=val:
                nums[pointer1],nums[pointer2]=nums[pointer2],nums[pointer1]
            elif nums[pointer1]==val and nums[pointer2]==val:
                pointer2+=1
                continue
            pointer2+=1
            pointer1+=1
        # print(k)
        # print(nums)
        return len(nums)-k 
        