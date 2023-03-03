class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        answer=right=sum(weights)

        while left<=right:
            mid=(left+right)//2
            curr=1
            load=mid
            for weight in weights:
                if load>=weight:
                    load-=weight
                else:
                    curr+=1
                    load=mid
                    load-=weight
            if curr<=days:
                answer=min(answer,mid)
                right=mid-1
            else:
                left=mid+1

        return answer