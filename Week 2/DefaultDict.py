# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

nums = list(map(int, input().split(" ")))
groupA = defaultdict(list)
groupB = []

for i in range(nums[0]):
    word = input()
    groupA[word].append(str(i+1))
for _ in range(nums[1]):
    groupB.append(input())
# print(groupA)


for word in groupB:

    if word in groupA:
        print(" ".join(groupA[word]))
    else:
        print(-1)
