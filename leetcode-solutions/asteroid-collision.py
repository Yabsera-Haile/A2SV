class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                ast1=abs(stack[-1])
                ast2=abs(ast)
                if ast1>ast2:
                    break
                elif ast1<ast2:
                    stack.pop()
                else:
                    stack.pop()
                    break
            else:
                stack.append(ast)
        
        return stack

        