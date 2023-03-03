class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_count=[]
        query_count=[]

        for word in words:
            word=list(word)
            word.sort()
            start=bisect_left(word,word[0])
            end=bisect_right(word,word[0])
            word_count.append(end-start)
        for query in queries:
            query=list(query)
            query.sort()
            start=bisect_left(query,query[0])
            end=bisect_right(query,query[0])
            query_count.append(end-start)
        word_count.sort()
        result=[]
        for query in query_count:
            end=bisect_right(word_count,query)
            result.append(len(word_count)-end)
        
        return result