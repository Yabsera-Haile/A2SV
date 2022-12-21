class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        short = min(strs, key=len) 
        for item in strs: 
            while len(short) > 0:
                if item.startswith(short):
                    break
                else:
                    short = short[:-1] 
        return short





# Brute Force
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         stack=[]
#         flag=0
#         for i in range(len(strs[0])):
#             for j in range(len(strs)):
#                 if i>=len(strs[j]):
#                     if stack and j!=0: 
#                         stack.pop()
#                     flag=flag+1
#                     break
#                 elif j==0: 
#                     stack.append(strs[j][i])
#                 elif strs[j][i]!=stack[-1]:
#                     if stack:
#                         stack.pop()
#                     flag=flag+1
#                     break
#             if flag>=1:
#                 break
#         return "".join(stack)
                    