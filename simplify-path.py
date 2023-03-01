class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        stack=[]

        for dir in path:
            if dir==".." and stack:
                stack.pop()
            elif dir!="." and dir!=".." and dir!="":
                stack.append(dir)
        print(stack)
        result=["/"]
        for i,s in enumerate(stack):
            result.append(s)
            if i!=len(stack)-1:
                result.append("/")

        return "".join(result)