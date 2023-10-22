import sys
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, ceil, lcm
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right, insort_left, insort_right
def ints(): return map(int, sys.stdin.readline().strip().split())
def li(): return list(map(int, sys.stdin.readline().strip().split()))
def string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def li_strings(): return list(map(str, sys.stdin.readline().strip().split()))

for _ in range(get_int()):
    n, m, k = ints()
    x = li()
    ladders = []
    dic = defaultdict(list)
    dic[1].append((1, 1, 1, 0))
    dic[n].append((m, n, m, 0))
    memo = {}
    for i in range(k):
        a, b, c, d, h = ints()
        memo[(a, b)] = float("inf")
        memo[(c, d)] = float("inf")
        dic[a].append((b, c, d, h))
        dic[c].append((d, c, d, 0))
        ladders.append((a, b, c, d, h))

    memo[(1, 1)] = 0
    for i in range(1, n + 1):
        cur = sorted(dic[i])

        for j in range(1, len(cur)):
            if (i, cur[j][0]) not in memo:
                memo[(i, cur[j][0])] = float("inf")
            memo[(i, cur[j][0])] = min(memo[(i, cur[j][0])],memo[(i, cur[j - 1][0])] + (cur[j][0] - cur[j - 1][0]) * x[i - 1])
        for j in range(len(cur) - 2, -1, -1):
            if (i, cur[j][0]) not in memo:
                memo[(i, cur[j][0])] = float("inf")

            memo[(i, cur[j][0])] = min(memo[(i, cur[j][0])],
                                    memo[(i, cur[j + 1][0])] + (cur[j + 1][0] - cur[j][0]) * x[i - 1])
        for j in range(len(cur)):
            if (cur[j][1], cur[j][2]) not in memo:
                memo[(i, cur[j][0])] = float("inf")

            memo[(cur[j][1], cur[j][2])] = min(
                memo[(cur[j][1], cur[j][2])], memo[(i, cur[j][0])] - cur[j][3])

    print(memo[(n, m)] if memo[(n, m)] != float('inf') else "NO ESCAPE")
