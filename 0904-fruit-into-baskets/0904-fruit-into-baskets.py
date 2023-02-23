class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=result=0
        picked={}
        
        for right,value in enumerate(fruits):
            picked[value]=picked.get(value,0)+1
            
            if len(picked)>2:
                picked[fruits[left]]-=1
                if picked[fruits[left]]<=0:
                    del picked[fruits[left]]
                left+=1  
            result=max(right-left+1,result)

        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = ans = 0
#         basket = {}
#         for i,j in enumerate(fruits):
#             basket[j] = basket.get(j,0) + 1
#             if len(basket)>2 :
#                 basket[fruits[l]] -= 1
#                 if(basket[fruits[l]]<=0):del basket[fruits[l]]
#                 l += 1
#             ans = max(ans,i-l+1)
#         return ans
        