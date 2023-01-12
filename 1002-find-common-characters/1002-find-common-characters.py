class Solution:
    def commonChars(self, words: List[str]) -> List[str]:       
        result = [0]*26
        offset = ord('a') 
        for letter in words[0]:
            curr = ord(letter)
            result[curr - offset] += 1   
            
        for word in words:
            temp = [0]*26
            for letter in word:
                curr = ord(letter)
                temp[curr - offset] += 1  
                
            for i in range(26):
                result[i]=min(temp[i],result[i])                                  
        answer=[]       
        for index,count in enumerate(result):
            if count!=0:
                current=chr(index+offset)
                answer.extend([current]*count)
            
        return list(answer)

                
        