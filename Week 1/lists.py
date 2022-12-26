if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        read = input().split(" ")
        if read[0] == "insert":
            result.insert(int(read[1]), int(read[2]))
        elif read[0] == "print":
            print(result)
        elif read[0] == "remove":
            result.remove(int(read[1]))
        elif read[0] == "append":
            result.append(int(read[1]))
        elif read[0] == "sort":
            result.sort()
        elif read[0] == "pop":
            result.pop()
        elif read[0] == "reverse":
            result.reverse()
