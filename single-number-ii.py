class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp=0
        neg=0

        for num in nums:
            if num<0:
                neg+=1
            for i in range(num.bit_length()):
                if temp//(10**i)%10==9:
                    temp-=(9*10**i)
                temp+=(int(bin(num)[-(i+1)])*(10**i))
                
        result=0
        for num in str(temp):
           if int(num)%3==1:
               result<<=1
               result|=1
           else:
               result<<=1

        if neg%3==0:
            return result
        else:
            return -result