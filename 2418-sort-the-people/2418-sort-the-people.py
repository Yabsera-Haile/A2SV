class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            j=heights.index(max(heights[i:]))
            heights[i],heights[j]=heights[j],heights[i]
            names[i],names[j]=names[j],names[i]             
        return names
                    
        
        