t=int(input())
for _ in range(t):
    string=input()
    result=[]
    index=0
    while index<len(string)-1:
        if string[index] == string [index +1]:
            index+=2
        else:
            result.append(string[index])
            index+=1
    if index==len(string)-1:
        result.append(string[-1])
    result=list(set(result))   
    result.sort()
    print("".join(result))