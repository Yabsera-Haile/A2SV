class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result, n = float('inf'), len(nums)
        for i in range(n-2):
            S1 = nums[i] + nums[i+1] + nums[i+2]
            S2 = nums[i] + nums[n-2] + nums[n-1]
            candidates = [result, S1, S2]
            result = min(candidates, key = lambda x: abs(x-target))            
            if S1 <= target <= S2:
                left, right = i+1, n-1
                while left < right:
                    S = nums[i] + nums[left] + nums[right]
                    candidates = [result, S]
                    result = min(candidates, key = lambda x: abs(x-target))
                    if S == target:
                        return target
                    elif S < target:
                        left += 1
                    else:
                        right -= 1
        return result