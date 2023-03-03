class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left=1
        right=piles[-1]
        answer=right
        while left<=right:
            mid=(left+right)//2
            result=0
            for pile in piles:
                result+=math.ceil(pile/mid)
            if result<= h:
                answer=min(answer,mid)
                right=mid-1
            else:
                left=mid+1

        return answer