from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ref=dict(Counter(s))
        count={}
        stack=[]
        for letter in s:
            if letter in stack:
                ref[letter]-=1
                continue
            while stack and stack[-1]> letter and ref[stack[-1]]>0:
                curr=stack.pop()
            ref[letter]-=1
            stack.append(letter)

        return "".join(stack)