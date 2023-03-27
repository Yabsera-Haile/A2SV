from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        _sorted=SortedList()
        result=0

        for num in nums:
            if _sorted:
                curr=bisect_right(_sorted,2*num)
                result+=(len(_sorted)-curr)
            _sorted.add(num)
        
        return result