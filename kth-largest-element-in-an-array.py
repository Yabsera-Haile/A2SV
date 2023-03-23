class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(left,right):
            if left<right:
                pivot=partition(left,right)
                if len(nums)-pivot<k:
                    quickSort(left,pivot-1)
                elif len(nums)-pivot>k:
                    quickSort(pivot+1,right)

            
        
        def partition(left,right):
            greater=left-1

            for i in range(left,right):
                if nums[i]<=nums[right]:
                    greater+=1
                    nums[i],nums[greater]=nums[greater],nums[i]

            nums[greater+1],nums[right]=nums[right],nums[greater+1]

            return greater+1
            
        
        quickSort(0,len(nums)-1)
        return nums[-k]