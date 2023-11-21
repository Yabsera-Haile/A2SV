class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr=[0]+arr+[0]
        stack=[]
        result=0

        for i in range(len(arr)):
            while stack and arr[i]<arr[stack[-1]]:
                curr=stack.pop()
                result+=arr[curr]*(i-curr)*(curr-stack[-1])
            stack.append(i)

        return result % (10**9+7)

