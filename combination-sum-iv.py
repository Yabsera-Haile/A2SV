class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={}

        def findCombo(_sum):
            # print(index,_sum)
            if _sum>target:
                return 0
            if _sum==target:
                return 1
            if _sum not in memo:
                curr=0
                for i in range(len(nums)):
                    curr+=findCombo(_sum+nums[i])

                memo[_sum]=curr
            
            return memo[_sum]
        
        return findCombo(0)