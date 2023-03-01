class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper=["+","-","*","/"]
        stack=[]
        for token in tokens:
            if token in oper:
                num2=stack.pop()
                num1=stack.pop()
                if token=="+":
                    stack.append(num1+num2)
                elif token=="-":
                    stack.append(num1-num2)
                elif token=="*":
                    stack.append(num1*num2)
                elif token=="/":
                    if num1*num2>0:
                        stack.append(num1//num2)
                    else:
                        stack.append(math.ceil(num1/num2))
            else:
                stack.append(int(token))
        return stack[-1]