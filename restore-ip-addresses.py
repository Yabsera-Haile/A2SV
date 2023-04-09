class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
  
        def backtrack(index,address):
            if index==len(s):
                if len(address)==4:
                    result.append( '.'.join(map(str,address)) )
                return
            
            curr=address[-1]*10+int(s[index])
            if address[-1]!=0 and  curr<= 255:
                temp=address[-1]
                address[-1] =curr

                backtrack(index+1, address)                    
                address[-1] = temp
            
            if len(address)<4:
                address.append(int(s[index]))           
                backtrack(index+1,address)         
                address.pop()        
        
        backtrack(1,[int(s[0])])
        return result