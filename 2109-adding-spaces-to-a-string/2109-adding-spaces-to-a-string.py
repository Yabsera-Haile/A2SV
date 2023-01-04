class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=[]
        i=0
        for index,char in enumerate(s):
            if i<len(spaces) and index==spaces[i]:
                result.append(" ")
                result.append(char)
                i+=1
            else:
                result.append(char)
        return "".join(result)

            
        