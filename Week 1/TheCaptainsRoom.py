# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = input()
room_list = input()
hash_map = {}
result = Counter(room_list.split())
for key, item in result.items():
    if item == 1:
        print(key)
