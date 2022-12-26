class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        out_of_bound=0
        n=0
        while n < len(arr):
            if arr[n]==0:
                arr.insert(n+1,0)
                out_of_bound+=1
                n+=1
            n+=1
                
        for _ in range(out_of_bound):
            arr.pop()
        