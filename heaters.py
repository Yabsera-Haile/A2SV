class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        result=0

        for house in houses:
            index=bisect_left(heaters,house)
            if index == len(heaters):
                index-=1
                
            if index==0:
                result=max(abs(heaters[index]-house),result)
            else:
                diff=min(abs(heaters[index]-house),abs(heaters[index-1]-house))
                result=max(result,diff)
        
        return result