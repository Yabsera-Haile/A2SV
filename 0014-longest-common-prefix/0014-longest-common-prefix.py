class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack=[]
        flag=0
        for i in range(200):
            for j in range(len(strs)):
                if i>=len(strs[j]):
                    if stack and j!=0: 
                        stack.pop()
                    flag=flag+1
                    break
                elif j==0: 
                    stack.append(strs[j][i])
                elif strs[j][i]!=stack[-1]:
                    if stack:
                        stack.pop()
                    flag=flag+1
                    break
            if flag>=1:
                break
        return "".join(stack)
                    