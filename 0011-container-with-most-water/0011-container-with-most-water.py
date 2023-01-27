class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        sorted_height = sorted(range(len(height)), key=lambda k: height[k], reverse=True)
        left = sorted_height[0]
        right = sorted_height[0]
        for col in sorted_height:
            left = min(col, left)
            right = max(col, right)
            area=height[col] * max(col - left, right - col)
            result = max(result, area)
            
            if result > len(height) * height[col]:
                return result

        return result
                
    
