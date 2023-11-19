class Solution:
    def jump(self, nums: List[int]) -> int:
        #Greedy
        reach, count, last = 0, 0, 0
        
        for i in range(len(nums)-1):    
            reach = max(reach, i + nums[i])
            if i == last:
                last = reach
                count += 1

        return count
        
        # DP
        # n=len(nums)
        # dp=[float('inf') for _ in range(n)]
        # dp[0]=0
        # for i in range(n):
        #     for j in range(1,nums[i]+1):
        #         if i+j<n:
        #             dp[i+j]=min(dp[i+j],dp[i]+1)
        # return dp[n-1]
        