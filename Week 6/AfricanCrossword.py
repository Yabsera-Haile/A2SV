[n,m]=list(map(int,input().split()))
words=[]
for _ in range(n):
    words.append(list(input()))
count={}
for row in range(n):
    for col in range(m):
        if count.get((row,col),-1)==-1 :
            for i in range(n):
                if words[i][col]==words[row][col] and row!=i:
                    count[(i,col)]=1
                    count[(row,col)]=1
            for i in range(m):
                if words[row][i]==words[row][col] and col!=i:
                    count[(row,i)]=1
                    count[(row,col)]=1
                    
result=[]
for row in range(n):
    for col in range(m):
        if count.get((row,col),-1)==-1:
            result.append(words[row][col])
            
print("".join(result))
