class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def subsets(canidate,depth,first):
            if depth<=len(nums):
                result.append(canidate)

                for i in range(first,len(nums)):
                    canidate.append(nums[i])
                    subsets(canidate[::],depth+1,i+1)
                    canidate.pop()
        subsets([],0,0)
        return result
            