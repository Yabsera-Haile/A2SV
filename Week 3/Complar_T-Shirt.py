n = int(input())
for _ in range(n):
    sizes = input().split(" ")
    t1 = sizes[0]
    t2 = sizes[1]
    if t1[-1] > t2[-1]:
        print("<")
    elif t2[-1] > t1[-1]:
        print(">")
    elif t1[-1] == t2[-1]:
        if len(t1) > len(t2) and t1[-1] == "S":
            print("<")
        elif len(t1) < len(t2) and t1[-1] == "S":
            print(">")
        elif len(t1) > len(t2) and t1[-1] == "L":
            print(">")
        elif len(t1) < len(t2) and t1[-1] == "L":
            print("<")
        elif len(t1) == len(t2):
            print("=")
