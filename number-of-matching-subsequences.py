class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        class TrieNode:
            def __init__(self):
                self.children={}
                self.isEndOfWord=0
        
        class Trie:
            def __init__(self):
                self.root=TrieNode()
                self.count=0
            
            def addWord(self,word):
                curr=self.root
                
                for letter in word:
                    if letter not in curr.children:
                        curr.children[letter]=TrieNode()
                    curr=curr.children[letter]
                curr.isEndOfWord+=1
            
            def findPosition(self,word,index,letter):
                for i in range(index,len(word)):
                    if word[i] == letter:
                        return i
                return -1
            
            def findSubsequence(self,node,index,word):
                for i in range(26):
                    letter=chr(i+ord('a'))

                    if letter in node.children:
                        child=node.children[letter]
                        pos=self.findPosition(word,index,letter)

                        if pos!=-1:
                            self.count+=child.isEndOfWord
                            self.findSubsequence(child,pos+1,word)
        
        solution=Trie()
        for word in words:
            solution.addWord(word)
        
        solution.findSubsequence(solution.root,0,s)
        return solution.count