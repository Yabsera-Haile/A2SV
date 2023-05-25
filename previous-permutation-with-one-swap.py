class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        curr=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i-1]>arr[i]:
                curr=i-1
                break
        
        if curr!=-1:     
            for i in range(len(arr)-1,-1,-1):
                if arr[curr]>arr[i] and arr[i]!=arr[i-1]:
                    arr[curr],arr[i]=arr[i],arr[curr]
                    break

        return arr