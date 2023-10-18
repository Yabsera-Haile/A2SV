class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        _min=min(nums)
        _max=max(nums)
        return max(0,(_max-k)-(_min+k))