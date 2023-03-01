class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for index,char in enumerate(s):
            if char=="(":
                stack.append(char)
            elif stack[-1]=="(":
                stack.pop()
                stack.append(1)
            else:
                curr=0
                while stack[-1]!="(":
                    curr+=stack.pop()
                stack.pop()
                stack.append(2*curr)

        return sum(stack)