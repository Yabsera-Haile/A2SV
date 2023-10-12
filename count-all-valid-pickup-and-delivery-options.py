class Solution:
    def countOrders(self, n: int) -> int:
        mod=(10**9)+7
        @cache
        def findOptions(pick,delv):
            if pick==0 and delv==0:
                return 1

            if pick==delv:
                return findOptions(pick-1,delv)*pick

            if pick < delv:
                result=0
                if pick>0:
                    result+=(findOptions(pick-1,delv)*pick)

                result+=(findOptions(pick,delv-1)*(delv-pick))
                return result
    
        return findOptions(n,n) % mod