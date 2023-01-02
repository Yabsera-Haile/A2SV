class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        #initialize hashmap and count
        hashmap={}
        result=0
        
        #iterate
        for i in deliciousness:
            if len(hashmap)==0:
                hashmap[i]=0
            for j in range(22):
                if (2**j)-i in hashmap:
                    result+=hashmap[(2**j)-i]  
            if i not in hashmap:
                hashmap[i]=1
            elif i in hashmap or hashmap[i]==0:
                hashmap[i]+=1  
        return result % ((10**9)+7)     
                