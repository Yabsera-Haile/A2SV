from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums, x):

        if x == 0: return 0

        n, res, min_dist = len(nums), SortedList(), float("inf")

        for i in range(x,n):
            res.add(nums[i-x])

            idx = res.bisect_left(nums[i])

            if idx < len(res):
                min_dist = min(min_dist,abs(res[idx]-nums[i]))
            if idx > 0:
                min_dist = min(min_dist,abs(res[idx-1]-nums[i]))

        return min_dist

