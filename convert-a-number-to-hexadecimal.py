class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num = (1 << 32) + num
        
        ref = '0123456789abcdef'  
        
        result = ''  

        while num > 0:
            curr = num % 16  
            result = ref[curr] + result  
            num //= 16  
        
        return result