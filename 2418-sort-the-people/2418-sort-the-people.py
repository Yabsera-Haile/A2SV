class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)-1):
            unsorted=i+1
            for j in range(i,-1,-1):
                if heights[unsorted] > heights[j]:
                    heights[unsorted],heights[j]=heights[j],heights[unsorted]
                    names[unsorted],names[j]=names[j],names[unsorted]
                    unsorted-=1
        return names
                    
        
        