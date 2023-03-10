class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helperFunc(curr,index):
            # print(curr,index)
            if index==len(num) and len(curr)>=3:
                return True
            for i in range(index,len(num)):
                temp=int(num[index:i+1])
                if ((len(curr)<2 or curr[-1]+curr[-2]==temp) and 
                (num[index]!="0" or i==index)):
                    curr.append(temp)
                    result= helperFunc(curr,i+1)
                    curr.pop()
                    if result:
                        return result
            return False

        return helperFunc([],0)