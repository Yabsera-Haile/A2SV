class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        def checkHappy(friend,curr):
            for a,b in pairs:
                if friend!=a and rating[friend][a]<curr and rating[a][friend]<rating[a][b]:
                    return 1
                if friend !=b and rating[friend][b]<curr and rating[b][friend]<rating[b][a]:
                    return 1
            return 0

        rating=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                rating[i][preferences[i][j]]=j+1

        result=0
        for a,b in pairs:
            result+=checkHappy(a,rating[a][b])
            result+=checkHappy(b,rating[b][a])
        
        return result