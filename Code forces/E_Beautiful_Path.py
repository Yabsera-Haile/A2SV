[n, m] = list(map(int, input().split()))
path = []
S = []
T = []
for row in range(n):
    current = input()
    path.append(current)
    for col,letter in enumerate(current):
        if letter == "S":
            S = [row, col]
        elif letter == "T":
            T= [row,col]
result="No"
for col in range(m):
    start=S[0]
    mid=start+1
    end = T[0]
    if abs(end-start)>2:
        break
    if path[S[1]][start] == "." and mid == "." and end == ".":
        result="Yes"
        break
print(result)

    
            
