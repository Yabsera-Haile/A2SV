class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left=1
        right=citations[-1]
        result=0

        while left<=right:
            mid=(left+right)//2
            count=0
            for cite in citations:
                if cite>=mid:
                    count+=1
                    
            if count>=mid:
                result=max(result,mid)
                left=mid+1
            else:
                right=mid-1

        return result