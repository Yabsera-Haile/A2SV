class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i=0
        j=i+1
        while i< len(arr)-1:
            if arr[i]==2*arr[j] or arr[j]==2*arr[i]:
                return True
            elif j==len(arr)-1:
                i+=1
                j=i+1
            else:
                j+=1
        return False
            
        