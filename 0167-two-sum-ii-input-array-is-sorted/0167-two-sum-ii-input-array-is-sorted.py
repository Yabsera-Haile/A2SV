class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[0,0]
        left=0
        right=len(numbers)-1
        while left< right:
            add=numbers[left]+numbers[right]
            if add==target:
                result[0]=left+1
                result[1]=right+1
                break
            elif add> target:
                right-=1
            else:
                left+=1
        return result
        