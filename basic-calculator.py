class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        
        def calculate(index):
            exp=[]
            neg=False

            while index<n:
                if s[index] in (" ","+","-"):
                    neg=(s[index]=='-')^neg
                    index+=1
                    continue
                elif s[index]=='(':
                    temp=calculate(index+1)
                    index=temp[1]
                    exp.append(-int(temp[0]) if neg else int(temp[0]))
                    neg=False
                elif s[index]==')':
                    return [sum(exp),index+1]
                else:
                    curr=s[index]
                    index+=1
                    while index<n and s[index] not in ('+','-','(',')'):
                        if s[index]!=" ":
                            curr+=s[index]
                        index+=1
                    
                    exp.append(-int(curr) if neg else int(curr))
                    neg=False

            return [sum(exp),index+1]

        return calculate(0)[0]