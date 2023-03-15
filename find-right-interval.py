class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [-1] * len(intervals)
        ref= {}
        for index, value in enumerate(intervals):
            ref[value[0]] = index
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
     
        for i, interval in enumerate(intervals):
            index = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            if index != len(intervals):
                result[i] = ref[sorted_intervals[index][0]]
        
        return result