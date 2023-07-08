class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        result=0
        _sum=0
        for i in range(len(satisfaction)):
            _sum += satisfaction[i]
            if _sum < 0:
                break
            result += _sum

        return result