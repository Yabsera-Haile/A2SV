class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        @cache
        def findMatch(index1,index2):
            if index1==n and index2==m:
                return True 

            if index1>=n:
                while(index2<m-1) :
                    if p[index2+1] == "*" :
                        index2 += 2 
                    else:
                        return False 
                if index2>= m: 
                    return True 
                return False
                
            if index2>=m:
                return False
            
            a = False
            b = False
            
            if index2<m-1 :
                if p[index2+1] == "*" :
                    if s[index1] == p[index2] :
                        a = findMatch(index1+1,index2)
                    elif p[index2] == "." :
                        a = findMatch(index1+1,index2)
                    b = findMatch(index1 , index2+2) 
                elif p[index2] == "." :
                    a = findMatch(index1+1 , index2+1) 
                else:
                    if p[index2] == s[index1] :
                        a = findMatch(index1+1,index2+1)
                    else :
                        return False
            elif p[index2] == "." :
                a = findMatch(index1+1 , index2+1) 
            else:
                if p[index2] == s[index1] :
                    a = findMatch(index1+1,index2+1)
                else:
                    return False 
            return a or b

        return findMatch(0,0)
        

                
        