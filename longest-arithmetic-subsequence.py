class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        result = 2
        memo = [{} for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                memo[i][diff] = memo[j].get(diff, 1) + 1
                result = max(result, memo[i][diff])

        return result