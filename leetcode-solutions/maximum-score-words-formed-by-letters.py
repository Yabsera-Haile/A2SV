class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n=len(words)
        m=len(letters)

        @cache
        def findScore(index,seen):
            if index>=n:
                return 0

            new_seen=seen
            total=0
            count=Counter(words[index])
            for i in range(m):
                if not seen & (1<<i) and letters[i] in count and count[letters[i]]>0:
                    count[letters[i]]-=1
                    new_seen |= (1<<i)
                    pos=ord(letters[i])-ord('a')
                    total+=score[pos]
                    if count[letters[i]]==0:
                        del count[letters[i]]
            
            skip=findScore(index+1,seen)
            take=0
            if not count:
                take=findScore(index+1,new_seen)+total
            
            return max(skip,take)
        
        return findScore(0,0)

            
                    

        