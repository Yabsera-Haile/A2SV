class Solution:
    def compare(self,num1,num2):
        if num1==num2:
            return 0
        elif num1>num2:
            return 1
        else:
            return -1
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result=1
        left=0
        
        for i in range(1,len(arr)):
            curr=self.compare(arr[i-1],arr[i])
            
            if curr==0:
                left=i
            elif i==len(arr)-1 or curr * self.compare(arr[i],arr[i+1])!=-1:
                result=max(result,i-left+1)
                left=i
        return result
        