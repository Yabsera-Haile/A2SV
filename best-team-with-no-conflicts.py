class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n=len(scores)
        teams=[(ages[i],scores[i]) for i in range(n)]
        teams.sort()
        memo=[0]*n
        result=0
        for i in range(n):
            curr=teams[i][1]
            memo[i]=curr

            for j in range(i):
                if teams[j][1]<=curr:
                    memo[i]=max(memo[i],memo[j]+curr)
            result=max(result,memo[i])
            
        return result