class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self):
                self.children={}
                self.isEndOfWord=False
                self.freq=0

        class Trie:
            def __init__(self):
                self.root=TrieNode()
                
            def insert(self, word: str) -> None:
                curr=self.root
                for letter in word:
                    if letter not in curr.children:
                        curr.children[letter]=TrieNode()
                    curr=curr.children[letter]
                    curr.freq+=1
                    
                curr.isEndOfWord=True

            def findScore(self, word: str) -> int:
                curr=self.root
                result=0
                for letter in word:
                    curr=curr.children[letter]
                    result+=curr.freq

                return result
        
        solution=Trie()
        for word in words:
            solution.insert(word)

        result=[]
        for word in words:
            result.append(solution.findScore(word))
            
        return result