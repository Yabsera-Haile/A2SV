t=int(input())

for _ in range(t):
    num=int(input())
    
    if num==1:
        print(3)
    elif num%2==1:
        print(1)
    elif num.bit_count()==1:
        print(num+1)
    else:
        count=0
        while num%2==0:
            count+=1
            num>>=1
            
        print(1<<count)