import itertools
input_string = str(input())
ans = list(set(itertools.permutations(input_string, len(input_string))))
print(len(ans))
ans_keys = []
for i in ans:
    key = ''
    for j in i:
        key = key + j
    ans_keys.append(key)
ans_keys = sorted(ans_keys)
for a in ans_keys:
    print(a)
