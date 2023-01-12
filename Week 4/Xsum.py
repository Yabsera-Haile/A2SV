t = int(input())
for _ in range(t):
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]
    right = {}
    left = {}
    placement = []
    for row in range(n):
        placement.append(list(map(int, input().split())))

    for row in range(n):
        for col in range(m):
            sums = row+col
            diff = row-col
            curr_r = right.get(sums, 0)
            curr_l = left.get(diff, 0)
            right[sums] = curr_r + placement[row][col]
            left[diff] = curr_l + placement[row][col]
    result = 0
    for row in range(n):
        for col in range(m):
            sums = right.get(row+col, 0)
            diff = left.get(row-col, 0)
            current = sums+diff-placement[row][col]
            result = max(result, current)

    print(result)
