from string import ascii_lowercase
class Solution:
    def freqAlphabets(self, s: str) -> str:
        #initialize result and hashmap
        result=""
        reference={}
        
        #Fill the reference values
        for index,letter in enumerate(ascii_lowercase):
            if index < 9:
                reference[str(index+1)]=letter
            else:
                reference[str(index+1)+"#"]=letter
       
        #
        left=0
        right=left+2
        while left<len(s):
            if right<len(s) and s[right]=="#":
                result+=reference[s[left:right+1]]
                left+=3
                right=left+2
            else:
                result+=reference[s[left]]
                left+=1
                right+=1

                
        
        return result
  

                    
        