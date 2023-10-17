class Solution:
    def minimumDeletions(self, s: str) -> int:
        result=b_total=s.count('a')
        a_count=b_count=0

        for letter in s:
            a_count+=(letter=='b')
            b_count+=(letter=='a')

            curr=a_count+(b_total-b_count)
            result=min(result,curr)
        
        return result