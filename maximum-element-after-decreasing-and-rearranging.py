class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0]=1

        for i in range(1,len(arr)):
            num1=arr[i-1]
            num2=arr[i]

            if abs(num2-num1)>1:
                arr[i]=num1+1
        
        return arr[-1]