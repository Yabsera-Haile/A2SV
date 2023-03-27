from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result=[]
        _sorted=SortedList(nums)

        for num in nums:
            curr=0
            if _sorted:
                curr=bisect_left(_sorted,num)

            result.append(curr)
            _sorted.discard(num)
            
        return result