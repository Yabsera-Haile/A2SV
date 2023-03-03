
t=int(input())
 
for _ in range(t):
    [a,b]=list(map(int,input().split()))
    left=1
    answer=0
    right=(2*a)+(2*b)
    
    while left<=right:
        mid=(left+right)//2
        left_a=a-mid
        left_b=b-mid
        total=left_a+left_b
        if left_b>=0 and left_a>=0 and total>=(2*mid):
            left=mid+1
            answer=max(mid,answer)
        else:
            right=mid-1
    print(answer)        