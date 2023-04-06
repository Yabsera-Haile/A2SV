class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def findOR(nums):
            curr=0
            for num in nums:
                curr|=num
            return curr

        _max=findOR(nums)
        result=0
        bit=0
        def subset(index,seen):
            nonlocal result,bit
            if len(seen)>0:
                # print(seen)
                if findOR(seen)==_max:
                    result+=1
            
            for i in range(index,len(nums)):
                if bit & (1<<i)==0:
                    seen.append(nums[i])
                    bit|=(1<<i)
                    subset(i+1,seen)
                    bit&=~(1<<i)
                    seen.pop()
        
        subset(0,[])

        return result