n=int(input())
cards=list(map(int,input().split()))

left=henok=wube=0
right=n-1

while left<=right:
    if cards[right]>cards[left]:
        wube+=cards[right]
        right-=1
    else:
        wube+=cards[left]
        left+=1
    if left>right:
        break
    if cards[right]>cards[left]:
        henok+=cards[right]
        right-=1
    else:
        henok+=cards[left]
        left+=1    
print(wube,henok)