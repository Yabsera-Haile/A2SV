n=int(input())

for i in range(n):
    row=list(map(int,input().split()))
    result=[]
    for j in range(n):
        if row[j]==1:
            result.append(str(j+1))
            
    print(len(result)," ".join(result))
        