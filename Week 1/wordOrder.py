import sys
input_text = sys.stdin
hash_map = {}
for line in input_text:
    hash_map[line.strip()] = hash_map.get(line.strip(), 0)+1
result = list(hash_map.values())
print(len(result[1:]))
print(' '.join(str(x) for x in result[1:]))
