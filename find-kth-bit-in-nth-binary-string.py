class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def changeString(string:str):
            string=list(string)
            for i in range(len(string)):
                if string[i]=="0":
                    string[i]="1"
                else:
                    string[i]="0"
            string.reverse()
            return "".join(string)
        
        def findString(n):
            if n==1:
                return "0"
            else:
                result=findString(n-1)
                # print(result,changeString(result))
                return result+"1"+changeString(result)
        
        result=findString(n)
        # print(result)
        return result[k-1]