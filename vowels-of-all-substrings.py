class Solution:
    def countVowels(self, word: str) -> int:
        n=len(word)
        mod=(10**9)+7
        vowels=set(['a','e','i','o','u'])
        result=0

        for i,letter in enumerate(word):
            if letter in vowels:
                result+=(i+1)*(n-i)
        
        return result