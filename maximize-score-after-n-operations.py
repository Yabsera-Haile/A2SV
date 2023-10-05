class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n=len(nums)

        @cache
        def findScore(oper,seen):
            if oper>n//2:
                return 0

            result=0
            for i in range(n):
                if not (seen & (1<<i)):
                    seen|=(1<<i)

                    for j in range(i+1,n):
                        if not seen & (1<<j):
                            seen|=(1<<j)
                            _gcd=math.gcd(nums[i],nums[j])*oper
                            result=max(result,_gcd+findScore(oper+1,seen))
                            seen&=~(1<<j)

                    seen&=~(1<<i)
            return result
                      
        return findScore(1,0)