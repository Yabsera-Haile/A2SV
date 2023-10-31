class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        count=defaultdict(list)

        for i in range(n):
            count[nums[i]].append(i)

        _max=max([len(value) for value in count.values()])

        result=min(value[-1]-value[0] for value in count.values() if len(value)==_max)
        return result+1
        