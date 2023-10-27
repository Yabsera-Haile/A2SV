class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            if hashmap.get(nums[i])==None:
                hashmap.update({target-nums[i]:i})
            else:
                return[i,hashmap.get(nums[i])]

            
