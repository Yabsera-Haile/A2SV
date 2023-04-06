n=int(input())

result=0
for i in range(n):
    row=list(map(int,input().split()))
    
    for j in range(i,n):
        if row[j]==1:
            result+=1

print(result)