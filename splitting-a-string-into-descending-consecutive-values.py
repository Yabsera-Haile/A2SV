class Solution:
    def splitString(self, s: str) -> bool:
        def helperFunc(curr,index):
            if index==len(s) and len(curr)>=2:
                return True
            for i in range(index,len(s)):
                temp=int(s[index:i+1])
                if not curr or curr[-1]-temp==1:
                    curr.append(temp)
                    result= helperFunc(curr,i+1)
                    curr.pop()
                    if result:
                        return result
            return False

        return helperFunc([],0)