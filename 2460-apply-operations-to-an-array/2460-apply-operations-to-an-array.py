class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        write = 0
        read = 1
        while read < len(nums):       
            if nums[write] == nums[read]:
                nums[write]*=2
                nums[read]=0
            write += 1
            read += 1
            
        write = 0
        read = 0
        while read < len(nums):       
            if nums[read] != 0:
                nums[read],nums[write]=nums[write],nums[read]
                write += 1
            read += 1

        return nums