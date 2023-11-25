class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot = sorted(robot)
        factory = sorted(factory)
        n= len(robot)
        m= len(factory)
        
        @cache
        def dp( i, j):
            if i >= n:  
                return 0
            
            if j >= m:
                return inf
            cost = 0
            ans = dp(i, j+1)  
            for k in range(min(n - i, factory[j][1])):
                cost += abs(robot[i+k] - factory[j][0])
                ans = min(ans, cost + dp(i+k+1, j+1))
            return ans

        return dp(0, 0)
        