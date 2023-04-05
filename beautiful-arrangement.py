class Solution:
    def countArrangement(self, n: int) -> int:
        result=0
        seen=0

        def backtrack():
            nonlocal seen, result
            if seen.bit_count()==n:
                result+=1
            
            for i in range(1,n+1):
                bit=seen.bit_count()+1
                if seen & (1<<i)==0 and (i%bit==0 or bit%i==0):
                    seen|=(1<<i)
                    backtrack()
                    seen&=~(1<<i)
                
        
        backtrack()
        return result