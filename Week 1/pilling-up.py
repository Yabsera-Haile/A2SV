# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *


def piling(blocks):
    while blocks:
        top = None
        if blocks[-1] > blocks[0]:
            top = blocks.pop()
        else:
            top = blocks.popleft()
        if len(blocks) == 0:
            return "Yes"
        if blocks[-1] > top or blocks[0] > top:
            return "No"


for i in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    print(piling(blocks))
