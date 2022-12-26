class Solution:
    #check weather even or odd
    def checkParity(self, num: int)-> bool:
        parity=False
        if num%2==0:
            parity=True
        return parity 
    
    
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #initialize pointers
        left=0
        right=1
        
        #swap all even numbers
        while right < len(nums):
            if self.checkParity(nums[left])==False and self.checkParity(nums[right]):
                nums[left],nums[right]=nums[right],nums[left]
            elif self.checkParity(nums[left])==False and self.checkParity(nums[right])==False:
                right+=1
                continue
            left+=1
            right+=1
        
        return nums
                
                