from collections import Counter
n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    planets = dict(Counter(input().split(" ")))
    for key, value in planets.items():
        count = planets[key]
        result = min(count, data[1])
        planets[key] = result
    print(sum(planets.values()))
