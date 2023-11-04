class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result=0
        hashmap=defaultdict(int)

        for word in words:
            if hashmap[word]>0:
                result+=4
                hashmap[word]-=1
            else:
                hashmap[word[::-1]]+=1
        
        if any(key[0]==key[1] and value>0 for key,value in hashmap.items()):
            return result+2
            
        return result
        