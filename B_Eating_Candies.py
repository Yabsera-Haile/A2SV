t=int(input())

for _ in range(t):
    n=int(input())
    candies=list(map(int,input().split()))
    left=sum1=sum2=0
    right=len(candies)-1
    result=0
    while left <= right:
        if sum1>sum2:
            sum2+=candies[right]
            right-=1
        elif sum2>sum1:
            sum1+=candies[left]
            left+=1
        if sum1 == sum2 :
            result=left+len(candies)-1-right
            sum2 += candies[right]
            sum1 += candies[left]
            left += 1
            right-= 1
    print(result)
        