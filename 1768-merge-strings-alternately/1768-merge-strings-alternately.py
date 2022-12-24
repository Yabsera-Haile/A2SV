class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #initialize pointers and result string
        pointer1=0
        pointer2=0
        result=""
        
        while pointer1<len(word1) or pointer2<len(word2):
            if pointer1==pointer2 and pointer1<len(word1):
                result+=word1[pointer1]
                pointer1+=1
            elif pointer2<len(word2):
                result+=word2[pointer2]
                pointer2+=1
            else:
                result+=word1[pointer1]
                pointer1+=1
        return result
            