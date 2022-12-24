from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #Build hashmaps to store the repitition
        repitition=""
        hashmap1=dict(Counter(t))
        hashmap2=dict(Counter(s))
        for key,value in hashmap1.items():
            if hashmap2.get(key,0)!=value:
                repitition+=key
        
        #Change strings to set
        set_t=set(t)
        set_s=set(s)
        #Find the difference between sets
        result=list(set_t-set_s)
        #If a letter is repeated it is stored in the hashmap so retrieve it
        if repitition:
            result.append(repitition)
        return str(result[0])
        