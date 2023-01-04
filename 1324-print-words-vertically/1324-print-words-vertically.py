from collections import defaultdict
class Solution:
    def printVertically(self, s: str) -> List[str]:
        ref=defaultdict(list)
        words=s.split(" ")
        sorted_words=sorted(words,key=len,reverse=True)
        length=len(sorted_words[0])

        for word in words:
            for index in range(length):
                if index<len(word):
                    ref[index].append(word[index])
                else:
                    ref[index].append(" ")
        result=[]
        for key,value in ref.items():
            while value[-1]==" ":
                value.pop()
            result.append("".join(value))
            
        return result
                
        