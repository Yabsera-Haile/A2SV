# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split(" "))
length = len(setA)
n = int(input())

result = True
for _ in range(n):
    current = set(input().split(" "))
    if len(current-setA) > 0 or len(setA-current) == 0:
        result = False
        break

print(result)
