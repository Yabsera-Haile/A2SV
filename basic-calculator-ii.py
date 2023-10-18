class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        oper=('+','-','*','/')
        exp=[]
        neg=False
        index=0
        while index<n:
            if s[index]==" " or s[index]=='+' or s[index]=='-':
                neg=(s[index]=='-')
                index+=1
                continue
            elif s[index] not in oper:
                curr=s[index]
                index+=1
                while index<n and s[index] not in oper:
                    if s[index]!=" ":
                        curr+=s[index]
                    index+=1
                exp.append(-int(curr) if neg else int(curr))
                neg=False
            else:
                num1=exp.pop()
                num2=s[index+1]
                op=index
                index+=2
                while index<n and s[index] not in oper:
                    if s[index]!=" ":
                        num2+=s[index]
                    index+=1
                num2=int(num2)
                if s[op]=='*':
                    exp.append(num1*num2)
                else:
                    exp.append(trunc(num1/num2))
            
        return sum(exp)