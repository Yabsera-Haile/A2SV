class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums,target)
        second = bisect_right(nums,target)
        if first == second:
            return [-1,-1]
        else:
            return [first,second-1]