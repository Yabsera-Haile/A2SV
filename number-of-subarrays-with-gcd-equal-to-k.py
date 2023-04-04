class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def findGCD(a,b):
            if b==0:
                return a

            return findGCD(b,a%b)
        
        result=0

        for i in range(len(nums)):
            gcd=nums[i]
            if gcd==k:
                result+=1
            for j in range(i+1,len(nums)):
                gcd=findGCD(gcd,nums[j])
                if gcd==k:
                    result+=1
                
        
        return result