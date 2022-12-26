class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #Create a hashmap of the location of the order
        reference={}
        for index,letter in enumerate(order):
            reference[letter]=index
        
        #Replace the letters of the word with the location on the reference
        words = [[reference[letter] for letter in word] for word in words]
        
        #Compare the number on each word and decide if the word is in correc order
        return all(word1 <= word2 for word1, word2 in zip(words, words[1:]))    
                
            
        