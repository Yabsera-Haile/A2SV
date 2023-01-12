class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        sums=sum([num for num in nums if num%2==0])
        for query in queries:
            [val,index]=query
            temp=nums[index]
            nums[index]+=val
            if temp%2==0 and nums[index]%2==0:
                change=nums[index]-temp
                sums+=change
            elif temp%2!=0 and nums[index]%2==0:
                sums+=nums[index]
            elif temp%2==0 and nums[index]%2!=0:
                sums-=temp
            result.append(sums)
        return result
        