class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph={chr(97+i):chr(97+i) for i in range(26)}
        inequality=[]

        def rep(x):
            if x==graph[x]:
                return x
            curr=rep(graph[x])
            graph[x]=curr
            return curr
        
        for equation in equations:
            a=equation[0]
            b=equation[3]
            if equation[1]=="=":
                parentA=rep(a)
                parentB=rep(b)
                if parentA!=parentB:
                    graph[parentB]=parentA  
            else:
                inequality.append(equation)
        
        for equation in inequality:
            a=equation[0]
            b=equation[3]
            parentA=rep(a)
            parentB=rep(b)
            if parentA==parentB:
                return False

        return True