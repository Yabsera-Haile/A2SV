# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
lenght = input()
arr = input().split()
like = input().split()
hate = input().split()
counts = dict(Counter(arr))
result = 0
for num in like:
    result += counts.get(str(num), 0)
for num in hate:
    result -= counts.get(str(num), 0)

print(result)
