class TrieNode:
    def __init__(self):
        self.children={}
        self.isWordEnd=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        curr=self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter]=TrieNode()
            curr=curr.children[letter]
        curr.isWordEnd=True
        
    def search(self, word: str) -> bool:
        return self.dfs(self.root,0,word)
    
    def dfs(self,node,index,word) -> bool:
        if index==len(word):
            return node.isWordEnd
        
        if word[index]==".":
            for child in node.children.values():
                if self.dfs(child,index+1,word):
                    return True

        if word[index] in node.children:
            return self.dfs(node.children[word[index]],index+1,word)

        return False

                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)