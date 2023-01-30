class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        products=0
        left=0
        right=len(skill)-1
        sums=skill[0]+skill[-1]
        while left<right:
            if skill[left] + skill[right] != sums:
                return -1
            else:
                products+=skill[left]*skill[right]
                left+=1
                right-=1
        return products
            
            
        