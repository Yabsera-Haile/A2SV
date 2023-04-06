n=int(input())
matrix=[]
sources=set()
sink=set()

for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(matrix)
    if max(row)==1:
        sources.add(i+1)
    
    for i,num in enumerate(row):
        if num==1:
            sink.add(i+1)

result1=[]
result2=[]

for i in range(n):
    if (i+1) not in sources and  (i+1) in sink:
        result1.append(str(i+1))
    elif (i+1) in sources and (i+1) not in sink:
        result2.append(str(i+1))
    elif (i+1) not in sources and (i+1) not in sink:
        result1.append(str(i+1))
        result2.append(str(i+1))

print(len(result2), " ".join(result2))
print(len(result1)," ".join(result1))




    