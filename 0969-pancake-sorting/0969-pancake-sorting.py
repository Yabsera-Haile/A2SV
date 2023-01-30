class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result=[]
        maxi=len(arr)
        temp=0
        while maxi>0:
            k=arr.index(maxi)
            arr[:k+1]=arr[:k+1][::-1]
            result.append(k+1)
            result.append(arr[0])
            arr[:arr[0]]=arr[:arr[0]][::-1]
            maxi-=1
        return result
            
        
            
                
        