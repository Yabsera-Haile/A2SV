class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        visited=0
        path=[]
        def backtrack():
            nonlocal visited
            if visited.bit_count()==len(nums):
                result.append(path[::])
                
            else:
                for i,num in enumerate(nums):
                    if visited & (1<<i) == 0:
                        visited |= (1<<i)
                        path.append(num)
                        backtrack()
                        visited &= ~(1<<i)
                        path.pop()
        backtrack()

        return result


        # result=[]

        # def backtrack(curr):
        #     if len(curr)==len(nums):
        #         result.append(curr)
        #     else:
        #         for num in nums:
        #             if num not in curr:
        #                 curr.append(num)
        #                 backtrack(curr[::])
        #                 curr.pop()
        # backtrack([])

        # return result