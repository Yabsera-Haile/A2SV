class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helperFunc(left,right,turn):
            if left==right:
                if turn==1:
                    return [nums[left],0]
                elif turn==2:
                    return [0,nums[left]]
            else:
                if turn == 1:
                    ans1=helperFunc(left+1,right,2)
                    ans1[0]+=nums[left]
                    ans2=helperFunc(left,right-1,2)
                    ans2[0]+=nums[right]
                    if ans1[0]>=ans2[0]:
                        return ans1
                    else:
                        return ans2
                elif turn ==2:
                    ans1=helperFunc(left+1,right,1)
                    ans1[1]+=nums[left]
                    ans2=helperFunc(left,right-1,1)
                    ans2[1]+=nums[right]
                    if ans1[1]>=ans2[1]:
                        return ans1
                    else:
                        return ans2
        result=helperFunc(0,len(nums)-1,1)
            
            
        if result[0]>=result[1]:
            return True
        else:
            return False
                
            