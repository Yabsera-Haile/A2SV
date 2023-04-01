from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        result=0
        _sorted=SortedList()

        for num in instructions:
            result+=min(_sorted.bisect_left(num),len(_sorted)-_sorted.bisect_right(num))
            result%=(10**9+7)
            _sorted.add(num)
        
        return result