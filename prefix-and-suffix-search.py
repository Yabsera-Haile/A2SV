class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False
        self.index=-1
class WordFilter:

    def __init__(self, words: List[str]):
        self.root=TrieNode()
        self.words=words

        for i,word in enumerate(words):
            curr=self.root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter]=TrieNode()
                curr=curr.children[letter]
            curr.index=i
            curr.isEndOfWord=True
   

    def f(self, pref: str, suff: str) -> int:
        curr=self.root
        
        for letter in pref:
            if letter not in curr.children:
                return -1
            curr=curr.children[letter]
        
        result=-1

        def dfs(node,word):
            nonlocal result
            if node.isEndOfWord:
                if word[len(word)-len(suff):] == suff:
                    result=max(result,node.index)
            for key,child in node.children.items():
                dfs(child,word+key)
        
        dfs(curr,pref)
        
        return result
            
            
            
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)