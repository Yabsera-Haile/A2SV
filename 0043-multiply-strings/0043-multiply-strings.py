class Solution:
    #function that converst string to int
    def convert(self, num: str)->str:
        result=0
        #defince hasmap
        hashmap={str(i):i for i in range(10)}
        for n in num:
            current=hashmap.get(n)
            result=result*10+current
        return result
        
    def multiply(self, num1: str, num2: str) -> str:
        #
        num1=self.convert(num1)
        num2=self.convert(num2)
        return str(num1*num2)

        
        
        
        
        