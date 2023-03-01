class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*len(nums)

        for request in requests:
            prefix[request[0]]+=1
            if request[1]!=len(nums)-1:
                prefix[request[1]+1]-=1
        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
        result=0
        prefix.sort()
        nums.sort()
        for i in range(len(nums)):
            result+=(prefix[i]*nums[i])
        
        return result%(10**9 + 7)