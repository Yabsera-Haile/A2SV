class Solution:
    def longestWord(self, words: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children={}
                self.isEndOfWord=False

        class Trie:
            def __init__(self):
                self.root=TrieNode()
                self.longest=""

            def insert(self, word) -> None:
                curr=self.root
                for letter in word:
                    if letter not in curr.children:
                        curr.children[letter]=TrieNode()
                    curr=curr.children[letter]        
                curr.isEndOfWord=True
            
            def findLongestWord(self,node,word):
                if len(self.longest)<len(word):
                    self.longest=word
                elif len(self.longest)==len(word) and word<self.longest:
                    self.longest=word
                
                for key,child in node.children.items():
                    if child.isEndOfWord:
                        self.findLongestWord(child,word+key)
        
        solution=Trie()
        for word in words:
            solution.insert(word)
        solution.findLongestWord(solution.root,"")
        return solution.longest