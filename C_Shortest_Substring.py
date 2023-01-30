t = int(input())

for _ in range(t):
    string = input()
    count = [-1, -1, -1]
    result = len(string)
    for index, char in enumerate(string):
        if char == "1":
            count[0] = index
        elif char == "2":
            count[1] = index
        elif char == "3":
            count[2] = index
        if -1 not in count:
            current = max(count)-min(count)+1
            result = min(result, current)

    if sorted(list(set(string))) == ['1', '2', '3']:
        print(result)
    else:
        print(0)
